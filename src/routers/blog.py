from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models


router = APIRouter()


@router.get("/blog", tags=["blogs"], response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs
