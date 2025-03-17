from apify import Actor
from apify_client import ApifyClient
import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.gemini import GeminiModel
from pydantic_ai.settings import ModelSettings
import math
from datetime import datetime
# import json

from .prompts import LINKEDIN_PROFILE_ANALYZER_SYSTEM_PROMPT, JOB_COACHING_SYSTEM_PROMPT
from .models import LinkedInProfileAnalysisResult, JobCoachingResult
from .tools import get_linkedin_profile_info, search_linkedin_jobs

load_dotenv()

apify_api_key = os.getenv("APIFY_API_KEY")
client = ApifyClient(apify_api_key) 

gemini_flash_2_model = GeminiModel('gemini-2.0-flash', provider='google-gla')

linkedin_profile_agent = Agent(
    gemini_flash_2_model,
    system_prompt = LINKEDIN_PROFILE_ANALYZER_SYSTEM_PROMPT,
    result_type=LinkedInProfileAnalysisResult,
    model_settings=ModelSettings(temperature=0),
)

job_coaching_agent = Agent(
    gemini_flash_2_model,
    system_prompt = JOB_COACHING_SYSTEM_PROMPT,
    result_type=JobCoachingResult,
    model_settings=ModelSettings(temperature=0),
)

def generate_markdown_report(
    profile_info: dict,
    selected_job_titles: list[str],
    selected_jobs: list[dict],
    summary: str
) -> str:
    """Generate a comprehensive markdown report of the job search results.
    
    Args:
        profile_info: The LinkedIn profile information
        selected_job_titles: List of suggested job titles
        selected_jobs: List of selected jobs with details
        summary: Executive summary of the job selection
        
    Returns:
        A markdown formatted report string
    """
    report = f"""# Job Search Report for {profile_info.get('firstName', '')} {profile_info.get('lastName', '')}
Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Profile Overview
- **Current Headline**: {profile_info.get('headline', 'N/A')}
- **Location**: {profile_info.get('addressWithoutCountry', '')}, {profile_info.get('addressCountryOnly', '')}
- **LinkedIn URL**: {profile_info.get('linkedinUrl', 'N/A')}

## Suggested Job Titles
Based on your profile analysis, here are the most relevant job titles for your background:

{chr(10).join(f'- {title}' for title in selected_job_titles)}

## Selected Job Opportunities

{chr(10).join(f'''### {job.get('title', 'N/A')} at {job.get('company', 'N/A')}
**Location**: {job.get('location', 'N/A')}
**Job ID**: {job.get('job_id', 'N/A')}

#### Why This Role?
{job.get('reason', 'N/A')}

#### Cover Letter
{job.get('cover_letter', 'N/A')}

---''' for job in selected_jobs)}

## Executive Summary
{summary}
"""
    return report

async def main() -> None:
    async with Actor:
        actor_input = await Actor.get_input() 
        
        await Actor.charge('init', 1)
        
        linkedin_profile_url = actor_input.get("linkedin_profile_url")
        
        # Perform the search
        linkedin_profile_info = await get_linkedin_profile_info(linkedin_profile_url=linkedin_profile_url)
        
        # Save the profile info to KV store
        kv_store = await Actor.open_key_value_store()
        await kv_store.set_value('linkedin_profile', linkedin_profile_info)
        
        # Analyze the profile
        linkedin_profile_analysis = await linkedin_profile_agent.run(f"Analyze this LinkedIn profile and return the 5 most relevant job titles.\n\n{linkedin_profile_info}")
        Actor.log.info(f"Suggested job titles: {linkedin_profile_analysis.data.relevant_job_titles}")
        
        # Charge for token usage
        usage = linkedin_profile_analysis.usage()
        await Actor.charge(event_name='1k-llm-tokens', count=math.ceil(usage.total_tokens / 1000))
        
        # Use the location from the profile info if available, otherwise use a default
        location = linkedin_profile_info.get("addressWithoutCountry")
        if location:
            location = f"{location}, {linkedin_profile_info.get('addressCountryOnly')}"
        else:
            location = linkedin_profile_info.get("addressCountryOnly", "United States")
                
        # Search for jobs for each relevant job title
        linkedin_jobs = []
        for job_title in linkedin_profile_analysis.data.relevant_job_titles:
            jobs_for_title = await search_linkedin_jobs(job_title=job_title, location=location)
            linkedin_jobs.extend(jobs_for_title)
            
        Actor.log.info(f"Found a total of {len(linkedin_jobs)} jobs across all relevant job titles")
        
        # Create a mapping of job IDs to full job details for later use
        job_details_map = {job.get("job_id", ""): job for job in linkedin_jobs if job.get("job_id")}
        
        # Run the job coaching agent to select the most relevant jobs and create cover letters
        job_coaching_result = await job_coaching_agent.run(
            f"""
            Select the 5 most relevant and varied jobs, explain why each was selected, and write personalized cover letters for each.
            
            Given this LinkedIn profile:
            {linkedin_profile_info}
            
            And these potential job opportunities:
            {linkedin_jobs}
            """
        )
        
        # Charge for token usage
        usage = job_coaching_result.usage()
        await Actor.charge(event_name='1k-llm-tokens', count=math.ceil(usage.total_tokens / 1000))
        
        # Get the full job details for each selected job
        selected_jobs_with_details = []
        for selected_job in job_coaching_result.data.selected_jobs:
            job_id = selected_job.job_id
            job_details = job_details_map.get(job_id, {})
            
            # Combine the job details with the reason and cover letter
            complete_job_info = {
                **job_details,
                "reason": selected_job.reason,
                "cover_letter": selected_job.cover_letter
            }
            selected_jobs_with_details.append(complete_job_info)
        
        # Store the selected jobs and cover letters
        await kv_store.set_value('selected_jobs_with_details', selected_jobs_with_details)
        
        # Generate the markdown report
        markdown_report = generate_markdown_report(
            profile_info=linkedin_profile_info,
            selected_job_titles=linkedin_profile_analysis.data.relevant_job_titles,
            selected_jobs=selected_jobs_with_details,
            summary=job_coaching_result.data.summary
        )
        
        # Store the markdown report in the KV store
        await kv_store.set_value('markdown_report', markdown_report)
        
        # Prepare the final output structure
        final_output = {
            "linkedin_profile_info": linkedin_profile_info,
            "selected_job_titles": linkedin_profile_analysis.data.relevant_job_titles,
            "selected_jobs": selected_jobs_with_details,
            "summary": job_coaching_result.data.summary,
            "markdown_report": markdown_report
        }
        
        # Push the results to Apify
        await Actor.push_data(final_output)
