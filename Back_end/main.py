from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from openai import OpenAI
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
print("API_KEY carregada:", api_key)

if not api_key:
    raise RuntimeError("OPENAI_API_KEY não encontrada no ambiente!")


client = OpenAI(api_key=api_key)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoLink(BaseModel):
    url: str


def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    else:
        return None


@app.post("/resumir")
def resumir_video(data: VideoLink):
    video_id = extract_video_id(data.url)
    if not video_id:
        raise HTTPException(status_code=400, detail="URL inválida")

    try:
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=['pt-BR', 'pt', 'en-US', 'en']
        )
        full_text = " ".join([t["text"] for t in transcript])

    except (TranscriptsDisabled, NoTranscriptFound) as e:
        raise HTTPException(
            status_code=500,
            detail=f"Não foi possível obter a transcrição: {str(e)}"
        )

    prompt = f"Resuma o conteúdo a seguir em tópicos claros e objetivos, como se explicasse para um estudante:\n\n{full_text}"

    try:
       
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que resume vídeos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        resumo = response.choices[0].message.content

        return {
            "resumo": resumo
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar resumo: {str(e)}")


@app.get("/")
def read_root():
    return {"message": "API está funcionando!"}
