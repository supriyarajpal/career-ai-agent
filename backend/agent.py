from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models import CareerRoadmap

# ✅ CORRECT constructor for v1.44
model = OpenAIModel("gpt-4o-mini")

agent = Agent(
    model,
    result_type=CareerRoadmap,
    system_prompt=(
        "You are a career guidance AI. "
        "Given a student's profile, generate a structured career roadmap "
        "with skills, weekly plan, and next steps."
    )
)








