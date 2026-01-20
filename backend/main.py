from fastapi import FastAPI, HTTPException
from agent import agent
from models import StudentProfile, RoadmapResponse
import json

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/roadmap", response_model=RoadmapResponse)
async def generate_roadmap(profile: StudentProfile):
    try:
        prompt = f"""
Education: {profile.education}
Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Hours per week: {profile.hours_per_week}
"""

        result = await agent.run(prompt)

        # pydantic-ai returns text → convert to JSON
        return json.loads(result.data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )



