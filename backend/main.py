from fastapi import FastAPI
from agent import agent
from models import StudentProfile, CareerRoadmap
import json

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/roadmap", response_model=CareerRoadmap)
async def generate_roadmap(profile: StudentProfile):
    prompt = f"""
Education: {profile.education}
Skills: {profile.skills}
Career Goal: {profile.career_goal}
Hours per week: {profile.hours_per_week}
"""

    result = await agent.run(prompt)

    # 👇 THIS LINE FIXES THE 500 ERROR
    data = json.loads(result.output_text)

    return CareerRoadmap(**data)









