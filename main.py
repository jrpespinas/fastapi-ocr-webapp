from fastapi import FastAPI
from model import nlp
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def read_main():
    return {"message": "Hello World"}


class Article(BaseModel):
    content: str


@app.post('/article/')
def analyze_article(article: Article):
    return article
