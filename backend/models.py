from pydantic import BaseModel
from typing import List, Dict

class StudentProfile(BaseModel):
    education: str
    skills: List[str]
    career_goal: str
    hours_per_week: int

class CareerRoadmap(BaseModel):
    career_options: List[str]
    required_skills: List[str]
    weekly_plan: Dict[str, List[str]]
    next_7_days: List[str]
