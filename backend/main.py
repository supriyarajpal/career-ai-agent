from fastapi import FastAPI, HTTPException
from models import StudentProfile, CareerRoadmap
from agent import agent

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/roadmap", response_model=CareerRoadmap)
async def generate_roadmap(profile: StudentProfile):
    try:
        result = await agent.run(
            f"""
            Education: {profile.education}
            Skills: {', '.join(profile.skills)}
            Career Goal: {profile.career_goal}
            Hours per week: {profile.hours_per_week}
            """
        )
        return result.output
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )
