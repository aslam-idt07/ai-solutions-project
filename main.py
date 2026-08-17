import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

app = FastAPI()

client = genai.Client(api_key=api_key)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_ai_response(request: PromptRequest):
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=request.prompt,
        )
        return {
            "status": "success",
            "user_prompt": request.prompt,
            "ai_response": response.text
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))