# Career AI Agent

A full-stack generative AI application that generates personalized career roadmaps for students using structured agent reasoning.

---

## Problem Statement

Students often struggle to understand which career paths suit them, what skills to learn, and how to plan their learning effectively.

---

## Solution

This application uses a Pydantic AI agent to:
- Analyze a student’s background and skills
- Reason about suitable career paths
- Generate a structured, actionable career roadmap

---

## Tech Stack

### Backend
- Python 3.11
- FastAPI
- Pydantic AI
- Pydantic v2
- Uvicorn

### Frontend
- Next.js
- Tailwind CSS

### Deployment
- Render (Backend)
- GitHub (Source Control)

---

## Architecture

User → Frontend (Next.js)  
→ Backend API (FastAPI)  
→ Pydantic AI Agent  
→ LLM Provider (OpenRouter / OpenAI compatible)  
→ Structured JSON response

---

## Agent Design

The agent is built using **Pydantic AI**, ensuring:
- Strong input validation
- Typed, structured outputs
- Reliable agent orchestration
- Clear system prompts

---

## API Endpoint

### POST /roadmap

#### Sample Request
```json
{
  "education": "BTech Computer Science",
  "skills": ["Python", "DSA", "SQL"],
  "career_goal": "AI Engineer",
  "hours_per_week": 15
}

⚠️ **Make sure there are THREE backticks ``` after the JSON and nothing extra inside**

---

## ✅ STEP 2 — SAVE → COMMIT → PUSH

Run these **exact commands**:

```bash
git add README.md
git commit -m "Fix README formatting and finalize submission"
git push
