from fastapi import FastAPI
from agent import agent
from models import StudentProfile, CareerRoadmap

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/roadmap")
async def generate_roadmap(profile: StudentProfile):
    result = await agent.run(
        profile.model_dump(),
        result_type=CareerRoadmap
    )
    return result.data








