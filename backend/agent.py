from pydantic_ai import Agent

agent = Agent(
    model="gpt-4o-mini",
    system_prompt="""
You are a career guidance AI.
Generate a clear, structured career roadmap.
Respond ONLY in valid JSON with these fields:
- career_options (list of strings)
- required_skills (list of strings)
- weekly_plan (object: week -> tasks)
- next_7_days (list of strings)
"""
)








