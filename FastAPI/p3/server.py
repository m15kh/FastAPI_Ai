from fastapi import FastAPI, status
from fastapi.responses import StreamingResponse
from models import load_audio_model, generate_audio ,VoicePresets
from utils import audio_array_to_buffer
from typing import Literal





@app.get("/generate/audio",
responses={status.HTTP_200_OK: {"content": {"audio/wav": {}}}},
response_class=StreamingResponse,
)
def serve_text_to_audio_model_controller(
prompt: str,
preset: VoicePresets = "v2/en_speaker_1",
):
    processor, model = load_audio_model()
    output, sample_rate = generate_audio(processor, model, prompt, preset)
    return StreamingResponse(audio_array_to_buffer(output, sample_rate), media_type="audio/wav")