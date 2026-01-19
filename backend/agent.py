from pydantic_ai import Agent
from models import RoadmapResponse

agent = Agent(
    model=model,
    result_type=RoadmapResponse,
    system_prompt="""
    You are a career guidance AI.
    Given a student's background, return a structured roadmap.
    """
)






