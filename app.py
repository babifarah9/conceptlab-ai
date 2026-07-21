from __future__ import annotations
import json
import os
import re
import uuid
from typing import Any, Optional

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()

app = FastAPI(title="ConceptLab AI", version="0.1.0")
app.mount("/static", StaticFiles(directory="static"), name="static")

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")
client = OpenAI() if os.getenv("OPENAI_API_KEY") else None
published_lessons: list[dict[str, Any]] = []


class LessonRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=160)
    level: str = Field(default="Beginner", max_length=40)


class TeachBackRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=160)
    explanation: str = Field(min_length=5, max_length=5000)


class PublishRequest(BaseModel):
    lesson: dict[str, Any]
    learner_explanation: str = ""
    evaluation: Optional[dict[str, Any]] = None


def extract_json(text: str) -> dict[str, Any]:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise ValueError("The model did not return valid JSON.")
        return json.loads(match.group(0))


def require_client() -> OpenAI:
    if client is None:
        raise HTTPException(
            status_code=503,
            detail="OPENAI_API_KEY is not configured. Add it to .env and restart.",
        )
    return client


@app.get("/")
def index():
    return FileResponse("static/index.html")


@app.get("/api/health")
def health():
    return {"status": "ok", "model": MODEL, "ai_configured": client is not None}


@app.post("/api/lesson")
def create_lesson(request: LessonRequest):
    ai = require_client()
    prompt = f"""
You are ConceptLab AI, an expert learning designer.

Create a concise, accurate, build-first lesson about "{request.topic}" for a
{request.level} learner. Return ONLY valid JSON with this exact structure:
{{
  "topic": "string",
  "level": "string",
  "hook": "one memorable sentence",
  "explanation": "2-4 short paragraphs in plain text",
  "analogy": "one useful analogy",
  "key_ideas": ["3-5 items"],
  "diagram": "a valid Mermaid flowchart using graph TD",
  "experiment": {{
    "title": "string",
    "instructions": ["3-5 steps"],
    "starter_code": "short runnable Python code",
    "things_to_change": ["2-3 parameters the learner can modify"]
  }},
  "quiz": [
    {{
      "question": "string",
      "options": ["A", "B", "C", "D"],
      "answer_index": 0,
      "explanation": "string"
    }}
  ],
  "teach_back_prompt": "one focused prompt asking the learner to explain it"
}}

Requirements:
- Include exactly 3 quiz questions.
- Keep code safe, deterministic, offline, and under 35 lines.
- Never invent citations.
- Make the experiment genuinely demonstrate the concept.
"""
    response = ai.responses.create(model=MODEL, input=prompt)
    try:
        lesson = extract_json(response.output_text)
    except (ValueError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return lesson


@app.post("/api/teachback")
def evaluate_teachback(request: TeachBackRequest):
    ai = require_client()
    prompt = f"""
You are a supportive but rigorous teacher evaluating a learner's teach-back.

Topic: {request.topic}
Learner explanation:
{request.explanation}

Return ONLY valid JSON:
{{
  "mastery_score": 0,
  "verdict": "Developing | Proficient | Strong",
  "strengths": ["2-3 specific strengths"],
  "gaps": ["0-3 specific missing or incorrect ideas"],
  "improved_explanation": "a corrected concise explanation",
  "next_challenge": "one practical next task"
}}

Score from 0 to 100. Do not reward confident wording when the content is wrong.
"""
    response = ai.responses.create(model=MODEL, input=prompt)
    try:
        result = extract_json(response.output_text)
    except (ValueError, json.JSONDecodeError) as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    return result


@app.post("/api/publish")
def publish(request: PublishRequest):
    item = {
        "id": str(uuid.uuid4())[:8],
        "lesson": request.lesson,
        "learner_explanation": request.learner_explanation,
        "evaluation": request.evaluation,
        "forks": 0,
        "likes": 0,
    }
    published_lessons.insert(0, item)
    return item


@app.get("/api/community")
def community():
    return published_lessons[:20]
