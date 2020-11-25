from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_main():
    return {"message": "Hello World"}


@app.get('/article/{article_id}')
def analyze_article(article_id: int):
    return {"article_id": article_id, "previous_id": article_id - 1}
