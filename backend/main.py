from fastapi import FastAPI
from models import StudentProfile
from agent import agent

app = FastAPI()

@app.post("/generate-roadmap")
async def generate_roadmap(profile: StudentProfile):
    result = await agent.run(profile)
    return result.data







