from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# ✅ model defined correctly
model = OpenAIModel("gpt-4o-mini")

# ✅ Agent has NO result_type
agent = Agent(
    model,
    system_prompt=(
        "You are a career guidance AI. "
        "Given a student's profile, generate a structured career roadmap."
    )
)








