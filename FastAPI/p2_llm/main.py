from fastapi import FastAPI
from models import generate_text, load_text_model


app = FastAPI()


@app.get("/generate/text")
def serve_llm_controller(prompt : str) -> str:
    pipe = load_text_model()
    response = generate_text(pipe, prompt)
    return response