from pydantic_ai import Agent

agent = Agent(
    model="gpt-3.5-turbo",
    system_prompt="""
    You are a professional career guidance counselor.
    Give realistic, practical, student-friendly advice.
    Always respond in structured format.
    """
)





