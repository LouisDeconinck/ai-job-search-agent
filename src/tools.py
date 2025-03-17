from apify import Actor
from apify_client import ApifyClient
import os

from typing import Dict, Any, List
from dotenv import load_dotenv

load_dotenv()

apify_api_key = os.getenv("APIFY_API_KEY")
client = ApifyClient(apify_api_key)

def safe_get(obj: Dict[str, Any], *keys: str) -> Any:
    """Safely get a nested value from a dictionary.
    
    Args:
        obj: Dictionary to get value from
        *keys: Sequence of keys to navigate through the nested dictionaries
        
    Returns:
        The value if found, None otherwise
    """
    current = obj
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current

async def get_linkedin_profile_info(linkedin_profile_url: str) -> Dict[str, Any]:
    """Get detailed information about a LinkedIn profile.
    
    Args:
        linkedin_profile_url: URL of the LinkedIn profile

    Returns:
        LinkedIn profile object with detailed information
    """
    Actor.log.info(f"Fetching details for {linkedin_profile_url}")
    
    run_input = {
        "profileUrls": [
            linkedin_profile_url
        ]
    }
    
    try:
        # Execute the actor and get the run info
        run = client.actor("dev_fusion/Linkedin-Profile-Scraper").call(run_input=run_input, memory_mbytes=512)
        
        all_items = client.dataset(run["defaultDatasetId"]).list_items().items
        
        if not all_items:
            return {}
            
        item = all_items[0]  # Just get the first item since we only process one URL
        
        # Extract data for experiences
        experiences = []
        for exp in item.get("experiences", []):
            experience = {
                "title": exp.get("title"),
                "subtitle": exp.get("subtitle"),
                "caption": exp.get("caption"),
            }
            
            # Extract the description directly from subcomponents
            for subcomp in exp.get("subComponents", []):
                for desc in subcomp.get("description", []):
                    if desc.get("type") == "textComponent":
                        experience["description"] = desc.get("text")
                        break
                if "description" in experience:
                    break
            
            experiences.append(experience)
        
        # Extract data for educations
        educations = []
        for edu in item.get("educations", []):
            education = {
                "title": edu.get("title"),
                "subtitle": edu.get("subtitle"),
                "caption": edu.get("caption"),
            }
            
            # Extract the description directly from subcomponents
            for subcomp in edu.get("subComponents", []):
                for desc in subcomp.get("description", []):
                    if desc.get("type") == "textComponent":
                        education["description"] = desc.get("text")
                        break
                if "description" in education:
                    break
            
            educations.append(education)
        
        # Extract data for licenses and certificates
        licenses = []
        for lic in item.get("licenseAndCertificates", []):
            license_cert = {
                "title": lic.get("title"),
                "subtitle": lic.get("subtitle"),
                "caption": lic.get("caption"),
            }
            licenses.append(license_cert)
        
        # Extract data for honors and awards
        honors = []
        for honor in item.get("honorsAndAwards", []):
            honor_award = {
                "title": honor.get("title"),
                "subtitle": honor.get("subtitle"),
            }
            
            # Extract the description directly from subcomponents
            for subcomp in honor.get("subComponents", []):
                for desc in subcomp.get("description", []):
                    if desc.get("type") == "textComponent":
                        honor_award["description"] = desc.get("text")
                        break
                if "description" in honor_award:
                    break
            
            honors.append(honor_award)
        
        # Extract data for languages
        languages = []
        for lang in item.get("languages", []):
            language = {
                "title": lang.get("title"),
                "caption": lang.get("caption"),
            }
            languages.append(language)
        
        # Extract data for volunteer and awards
        volunteer = []
        for vol in item.get("volunteerAndAwards", []):
            vol_award = {
                "title": vol.get("title"),
                "subtitle": vol.get("subtitle"),
                "caption": vol.get("caption"),
            }
            volunteer.append(vol_award)
        
        # Extract data for projects
        projects = []
        for proj in item.get("projects", []):
            project = {
                "title": proj.get("title"),
                "subtitle": proj.get("subtitle"),
            }
            
            # Extract the description directly from subcomponents
            for subcomp in proj.get("subComponents", []):
                for desc in subcomp.get("description", []):
                    if desc.get("type") == "textComponent":
                        project["description"] = desc.get("text")
                        break
                if "description" in project:
                    break
            
            projects.append(project)
        
        # Extract data for publications
        publications = []
        for pub in item.get("publications", []):
            publication = {
                "title": pub.get("title"),
                "subtitle": pub.get("subtitle"),
            }
            
            # Extract the description directly from subcomponents
            for subcomp in pub.get("subComponents", []):
                for desc in subcomp.get("description", []):
                    if desc.get("type") == "textComponent":
                        publication["description"] = desc.get("text")
                        break
                if "description" in publication:
                    break
            
            publications.append(publication)
        
        # Extract skills as an array of strings
        skills = [skill.get("title") for skill in item.get("skills", []) if skill.get("title")]
        
        # Create the filtered item with all requested fields
        filtered_item = {
            "firstName": item.get("firstName"),
            "lastName": item.get("lastName"),
            "headline": item.get("headline"),
            "addressCountryOnly": item.get("addressCountryOnly"),
            "addressWithoutCountry": item.get("addressWithoutCountry"),
            "about": item.get("about"),
            "experiences": experiences,
            "educations": educations,
            "licenseAndCertificates": licenses,
            "honorsAndAwards": honors,
            "languages": languages,
            "volunteerAndAwards": volunteer,
            "projects": projects,
            "publications": publications,
            "skills": skills,
            "linkedinUrl": item.get("linkedinUrl"),
        }
        
        Actor.log.info(f"Processed LinkedIn profile, found {len(experiences)} experiences, {len(educations)} educations, {len(licenses)} licenses, {len(honors)} honors, {len(languages)} languages, {len(volunteer)} volunteer, {len(projects)} projects, {len(publications)} publications, and {len(skills)} skills")
        
        await Actor.charge('tool-result', 1)
        return filtered_item
    except Exception as e:
        Actor.log.error(f"Error during LinkedIn profile retrieval: {str(e)}")
        return {}

async def search_linkedin_jobs(
    job_title: str,
    location: str,
) -> List[Dict[str, Any]]:
    """Search for LinkedIn jobs based on given parameters.
    
    Args:
        job_title: The job title to search for
        location: The location to search in
        
    Returns:
        List of job entries with detailed information
    """
    Actor.log.info(f"Searching LinkedIn jobs for '{job_title}' in '{location}'")
    
    run_input = {
        "job_title": job_title,
        "jobs_entries": 20,
        "location": location,
        "start_jobs": 0
    }
    
    try:
        # Execute the actor and get the run info
        run = client.actor("worldunboxer/rapid-linkedin-scraper").call(run_input=run_input, memory_mbytes=2048)
        
        # Get the dataset items
        all_items = client.dataset(run["defaultDatasetId"]).list_items().items
        
        Actor.log.info(f"Found {len(all_items)} LinkedIn jobs")
        
        await Actor.charge('tool-result', len(all_items))
        return all_items

    except Exception as e:
        Actor.log.error(f"Error during LinkedIn jobs search: {str(e)}")
        return []