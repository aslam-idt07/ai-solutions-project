import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai

app = FastAPI()

# Initialize the official Google GenAI client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

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