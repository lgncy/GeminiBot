from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()

# Configuring CORS
orig_origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orig_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/api/chat")
async def chat(request: ChatRequest):
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
    params = {
        'key': ''  #
    }
    headers = {
        'Content-Type': 'application/json',
    }

    # Prompt template
    prompt_template = (
        "User: {user_message}\n"
        "Your response:"
    )

    formatted_prompt = prompt_template.format(user_message=request.message)

    payload = {
        'contents': [
            {'parts': [{'text': formatted_prompt}]}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=payload)
    
    print("Response from Gemini:", response.json())  # Tambahkan ini untuk memeriksa respons
    return response.json()
