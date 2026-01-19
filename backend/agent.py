import os
from dotenv import load_dotenv
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel

# Force load environment variables
load_dotenv()

# Get and validate API key
api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key loaded: {api_key[:10]}..." if api_key else "API Key NOT FOUND!")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment!")

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