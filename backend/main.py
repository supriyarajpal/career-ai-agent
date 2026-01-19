from fastapi import FastAPI, HTTPException
from models import StudentProfile, CareerRoadmap
from agent import agent
import json

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/roadmap", response_model=CareerRoadmap)
async def generate_roadmap(profile: StudentProfile):
    try:
        # Create a detailed prompt
        prompt = f"""
Generate a career roadmap in JSON format for the following profile:

Education: {profile.education}
Skills: {', '.join(profile.skills)}
Career Goal: {profile.career_goal}
Hours Available: {profile.hours_per_week} hours per week

Return ONLY a valid JSON object with this exact structure:
{{
  "career_options": ["option1", "option2", "option3"],
  "required_skills": ["skill1", "skill2", "skill3"],
  "weekly_plan": ["task1", "task2", "task3"],
  "next_7_days": ["day1 task", "day2 task", "day3 task"]
}}

Make it practical and actionable based on {profile.hours_per_week} hours per week.
"""
        
        # Run the agent
        result = await agent.run(prompt)
        
        # Get the response text
        response_text = result.data if hasattr(result, 'data') else str(result)
        
        # Try to parse as JSON
        try:
            # If response_text is already a dict
            if isinstance(response_text, dict):
                roadmap_data = response_text
            else:
                # Clean the response (remove markdown code blocks if present)
                clean_text = response_text.strip()
                if clean_text.startswith("```"):
                    clean_text = clean_text.split("```")[1]
                    if clean_text.startswith("json"):
                        clean_text = clean_text[4:]
                clean_text = clean_text.strip()
                
                roadmap_data = json.loads(clean_text)
            
            # Validate and return
            return CareerRoadmap(**roadmap_data)
            
        except json.JSONDecodeError as je:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to parse AI response as JSON: {str(je)}"
            )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Roadmap generation failed: {str(e)}"
        )