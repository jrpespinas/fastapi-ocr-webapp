from fastapi import FastAPI
from model import nlp

app = FastAPI()


@app.get('/')
def read_main():
    return {"message": "Hello World"}


@app.post('/article/')
def analyze_article(): 
    return {} 
