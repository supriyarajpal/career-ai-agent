from fastapi import FastAPI, HTTPException
from models import StudentProfile, CareerRoadmap
from agent import agent
import json
import re

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


def extract_json(text: str) -> dict:
    """
    Safely extract JSON from LLM output
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("No JSON found in model output")
        return json.loads(match.group())


@app.post("/roadmap", response_model=CareerRoadmap)
async def generate_roadmap(profile: StudentProfile):
    prompt = f"""
Generate a career roadmap strictly as VALID JSON.

Rules:
- Output ONLY JSON
- No explanations
- No markdown
- No text before or after JSON

JSON format:
{{
  "career_options": [],
  "required_skills": [],
  "weekly_plan": {{}},
  "next_7_days": []
}}

Student details:
Education: {profile.education}
Skills: {profile.skills}
Career Goal: {profile.career_goal}
Hours per week: {profile.hours_per_week}
"""

    try:
        result = await agent.run(prompt)
        data = extract_json(result.output_text)
        return CareerRoadmap(**data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )









