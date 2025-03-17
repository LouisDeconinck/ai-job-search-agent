from pydantic import BaseModel, Field
from typing import List

class LinkedInProfileAnalysisResult(BaseModel):
    relevant_job_titles: List[str] = Field(
        description="List of maximum 5 relevant job titles that match the person's profile",
        max_items=5
    )

class SelectedJob(BaseModel):
    job_id: str = Field(description="The job_id of the selected job")
    reason: str = Field(description="The reason why the job was selected")
    cover_letter: str = Field(description="The cover letter for the job in markdown format")

class JobCoachingResult(BaseModel):
    selected_jobs: List[SelectedJob] = Field(
        description="List of 5, varied, most relevant jobs selected from the available jobs. Return the job_id.",
        max_length=5
    )
    summary: str = Field(description="An executive summary of the selected jobs.")