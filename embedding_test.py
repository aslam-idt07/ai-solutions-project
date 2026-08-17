import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

print("🔍 Google Server-la thedurom...")

for model in client.models.list():
    if "embed" in model.name.lower():
        print("✅ Correct Model Name:", model.name)
        