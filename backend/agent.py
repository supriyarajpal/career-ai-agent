from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# DO NOT pass api_key
# DO NOT pass base_url
# DO NOT pass headers
# pydantic-ai reads env vars automatically

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






