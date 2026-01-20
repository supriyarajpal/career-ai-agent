from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# DO NOT pass api_key, base_url, headers
# pydantic-ai reads them automatically from env

model = OpenAIModel(
    model_name="openai/gpt-4o-mini"
)

agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a structured, practical career roadmap."
    )
)






