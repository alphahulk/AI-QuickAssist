# Project Folder Structure
# ai-popup-extension/
# ├── backend/
# │   ├── app.py  # FastAPI Backend
# │   ├── requirements.txt  # Dependencies
# ├── extension/
# │   ├── content.js  # Handles text selection
# │   ├── background.js  # Communicates with popup
# │   ├── popup.js  # Handles UI logic
# │   ├── popup.html  # UI for the popup
# │   ├── manifest.json  # Chrome Extension Config
# ├── README.md

# backend/app.py - FastAPI Backend using Claude API

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os

app = FastAPI()

# Claude API Key (Set this in environment variables)
CLAUDE_API_KEY = os.getenv("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")
CLAUDE_API_URL = "https://api.anthropic.com/v1/messages"

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
