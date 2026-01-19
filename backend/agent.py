import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# pydantic-ai automatically reads:
# OPENAI_API_KEY
# OPENAI_BASE_URL

model = OpenAIModel(
    model_name="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    default_headers={
        "HTTP-Referer": "https://career-ai-agent-zojx.onrender.com",
        "X-Title": "Career AI Agent"
    }
)

agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a structured, practical career roadmap."
    )
)












