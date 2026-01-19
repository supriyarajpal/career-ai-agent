from fastapi import FastAPI, HTTPException
from models import StudentProfile
from agent import agent

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/roadmap")
async def generate_roadmap(profile: StudentProfile):
    try:
        prompt = f"""
Education: {profile.education}
Skills: {", ".join(profile.skills)}
Career Goal: {profile.career_goal}
Available hours per week: {profile.hours_per_week}

Generate a detailed career roadmap.
"""

        result = await agent.run(prompt)
        return result.output

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )

