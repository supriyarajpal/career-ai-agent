from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# IMPORTANT:
# OpenAIModel reads EVERYTHING from environment variables
# Do NOT pass api_key, base_url, headers, etc.

model = OpenAIModel(
    "gpt-4o-mini"
)

agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a clear, structured, and practical career roadmap."
    )
)


