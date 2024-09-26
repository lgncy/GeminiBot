# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx

app = FastAPI()

# Configuring CORS
orig_origins = [
    "http://localhost:3000",
    "https://porto-wildandwi-git-master-lgncys-projects.vercel.app",
    "https://porto-wildandwi-bv275qjbo-lgncys-projects.vercel.app"
    "https://wildandwi.my.id/"  # Ganti dengan URL frontend Anda
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
        'key': 'AIzaSyD7BOIiyfvJjRyu8qGbLDgzwhZNCzQHgec'  # Ganti dengan API Key Anda
    }
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'contents': [
            {'parts': [{'text': request.message}]}
        ]
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, params=params, json=payload)
    
    print("Response from Gemini:", response.json())  # Tambahkan ini untuk memeriksa respons
    return response.json()
