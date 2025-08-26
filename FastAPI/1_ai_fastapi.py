from fastapi import FastAPI
from openai import OpenAI
import yaml

with open ("/home/liam/own_project/fastapi/config.yaml", "r") as f :
    config =  yaml.safe_load(f)
    
api = config.get("api")

app = FastAPI()
openai_client = OpenAI(api_key=api,base_url="https://api.gilas.io/v1/" )


@app.get("/")
def root_controller():
    return {"stats":"healthy"}

@app.get("/chat")
def chat_controller(prompt: str = "inspire me"):
    response = openai_client.chat.completions.create(
    model  = 'gpt-4o',
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    
    )
    statment = response.choices[0].message.content
    return {"statement":statment}