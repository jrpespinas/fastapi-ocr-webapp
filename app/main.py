from fastapi import FastAPI
from src.database import engine
from src.routers import blog, user, authentication
from src import models

app = FastAPI()

# ROUTES
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)
