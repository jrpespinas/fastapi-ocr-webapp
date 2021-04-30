from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database
from ..repository import blog


router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.create_blog(request, db)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    return blog.get_blog_by_id(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    return blog.update_blog_by_id(id, request, db)


@router.delete("/{id}")
def destroy(id: int, db: Session = Depends(database.get_db)):
    return blog.delete_blog_by_id(id, db)
