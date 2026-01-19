from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models import CareerRoadmap

model = OpenAIModel(
    "gpt-4o-mini",
)

agent = Agent(
    model,
    system_prompt="""
You are a career guidance AI.
Return ONLY valid JSON that matches this schema:

{
  "career_options": [string],
  "required_skills": [string],
  "weekly_plan": { "Week 1": [string] },
  "next_7_days": [string]
}
"""
)









