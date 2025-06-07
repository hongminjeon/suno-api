from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_music(data: PromptRequest):
    # 실제 suno.ai 연동은 불가능하므로 데모 응답
    return {
        "status": "success",
        "prompt": data.prompt,
        "audio_url": "https://example.com/fake_suno_track.mp3"
    }
