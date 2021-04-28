from typing import List
from . import schemas, models
from .security import Hashing
from .database import engine, get_db
from .routers import blog, user
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, Response, HTTPException

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)

models.Base.metadata.create_all(engine)
