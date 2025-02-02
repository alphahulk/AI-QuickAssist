

# backend/app.py - FastAPI Backend using Claude API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Claude API Key (Set this in environment variables)
CLAUDE_API_KEY = os.getenv("Set this in environment variables")
CLAUDE_API_URL = "nil"

class QueryRequest(BaseModel):
    text: str

@app.post("/ai-response")
def get_ai_response(query: QueryRequest):
    if not CLAUDE_API_KEY:
        raise HTTPException(status_code=500, detail="Claude API Key not found")
    
    headers = {
        "x-api-key": CLAUDE_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "model": "claude-2",
        "prompt": query.text,
        "max_tokens": 200
    }
    
    response = requests.post(CLAUDE_API_URL, json=payload, headers=headers)
    
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    
    return {"response": response.json().get("completion", "No response from Claude")}

# requirements.txt
# fastapi
# uvicorn
# requests
