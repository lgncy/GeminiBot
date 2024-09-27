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
    "https://porto-wildandwi-bv275qjbo-lgncys-projects.vercel.app",  # Tambahkan koma di sini
    "https://wildandwi.my.id/",
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
        'key': 'AIzaSyD7BOIiyfvJjRyu8qGbLDgzwhZNCzQHgec'  # Ganti dengan API Key Anda
    }
    headers = {
        'Content-Type': 'application/json',
    }

    # Prompt template
    prompt_template = (
        "You are an AI assistant that provides helpful, detailed, and friendly responses. you are made to answer the data that has been provided. if the data does not exist then you respond to the data that does not exist with friendly speech.jawablah selalu menggunakan bahasa indonesia"
        "Kamu memiliki data yakni,kamu adalah wildan dwi Triatna Kusuma.kamu lahir pada tanggal 28 mei 2006 di malang dan kamu bersekolah di smkn 2 singosari,kamu adalah seorang yang ahli dalam bidang computer terlebihnya alam artificial intelligence dan prompt engineer.project yang pernah kamu buat yakni adalah tadbot yang berkaitan entang bot islam.kamu pernah mengikuti lks artificial intelligence di kabupaten dan provinsi.cewek kamu Bernama salwa alayda Yahya,nama user name ig kamu adalah wildandwoii dan username GitHub kamu adalah legancy.tinggi ildan adalah 170cm,setelah itu wildan adalah seorang anak pertama dari 2 bersaudara,nomer wa ku adalah +6281234384715.setelah itu kamu adalah seorang yang extrovert dan gampang bergaul dengan seseorang.Wildan juga jago dalam bidang pentester atau cybersecurity,wildan dulu pernah gabut atau iseng sampe sampe keisengannya buat web sekolahnya wildan menjadi down.dan wildan suka mencoba tentang exploitbug,xss,sql injection dan pokoknya yang berkaitan tentang itu,jadi wildan lebih enak di ajak membahas tentang ai dan cybersecurity.setelah itu wildan saying banget sama ceweknya,kayak ceweknya itu adalah motivasi buat wildan.jadii wildan akan selalu belajar belajar dan berusaha sampaii jagoo dan menguasai semuanyaa.tentang ceweknya wildan yakni salwa,salwa itu sekolah di smanela yaituu sma 1 lawang,salwa sangatt cantik an pintar..dia sekarang sedang belajar juga tentang utbk nya.hoby nya salwa itu scroll TikTok dan bobo,kalo wilda hobinya ngegame.salwa sangat periang,tanggal lahirnya salwa itu 22 juli 2006 dan berzodiak cancer,zodiaknya wildan itu gemini.salwa jago dalam Kimia dan juga fotografi,jadi kalo buat fotografi salwa jagonyaa,salwa pernah menang lomba fotografi jugaa di jakarta."
        "Here's the question from the user:\n\n"
        "User: {user_message}\n"
        "Your response:"
    )

    # Masukkan pesan pengguna ke dalam template
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
