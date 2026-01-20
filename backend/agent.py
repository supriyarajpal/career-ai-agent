from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# pydantic-ai reads auth ONLY from environment variables
# DO NOT pass api_key, base_url, headers here

model = OpenAIModel(
    model_name="gpt-4o-mini"
)

agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a structured, practical career roadmap."
    )
)



