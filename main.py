from fastapi import FastAPI
from model import nlp

app = FastAPI()


@app.get('/')
def read_main():
    return {"message": "Hello World"}


@app.get('/article/{article_id}')
def analyze_article(article_id: int, q: str = None):
    count = 0
    if q:
        doc = nlp(q)
        count = len(doc.ents)
    return {"article_id": article_id, "q": q, "count": count}
