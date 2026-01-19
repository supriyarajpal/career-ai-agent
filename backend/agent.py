from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# pydantic-ai reads everything from environment variables:
# OPENAI_API_KEY
# OPENAI_BASE_URL
# OPENAI_DEFAULT_HEADERS

model = OpenAIModel(
    model_name="openrouter/openai/gpt-4o-mini"
)

agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a structured, practical career roadmap."
    )
)

