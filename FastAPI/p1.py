from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional


class Register_User(BaseModel):
    name         : str = Path()
    last         : str
    age          : int
    phone_number : Optional[int]



app = FastAPI()




@app.get("/")
def index():
    return "hello form fast-api"


@app.get("/{name}/{age}")
def info(name :str, age: int):
    return {"message":f"hi {name} u are {age} years olds"}


@app.get("/{name}")
def query(name:str, age):
    return {"message":f"hi {name} u are {age} years olds"}

@app.post("/postt")
def postt(person : Register_User):
    return person
 