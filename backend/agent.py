import os
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from models import CareerRoadmap

# Environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")

# ✅ Correct OpenRouter-compatible model config
model = OpenAIModel(
    model_name="gpt-4o-mini",
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY,
    default_headers={
        "HTTP-Referer": "https://career-ai-agent-zojx.onrender.com",
        "X-Title": "Career AI Agent"
    }
)

# ✅ Agent (NO result_type here!)
agent = Agent(
    model=model,
    system_prompt=(
        "You are a career guidance AI. "
        "Generate a structured, practical career roadmap."
    )
)












