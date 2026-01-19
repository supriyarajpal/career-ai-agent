from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models import CareerRoadmap

# ✅ define the model FIRST
model = OpenAIModel(
    model="gpt-4o-mini",   # safe + cheap + supported
)

# ✅ now pass it into Agent
agent = Agent(
    model=model,
    result_type=CareerRoadmap,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a clear, structured learning roadmap."
    )
)







