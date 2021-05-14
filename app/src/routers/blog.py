from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, oauth2
from ..repository import blog


router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.create_blog(request, db)


@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.get_blog_by_id(id, db)


@router.put(
    "/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowSingleBlog
)
def update(
    id: int,
    request: schemas.Blog,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.update_blog_by_id(id, request, db)


@router.delete("/{id}")
def destroy(
    id: int,
    db: Session = Depends(database.get_db),
    current_user: schemas.User = Depends(oauth2.get_current_user),
):
    return blog.delete_blog_by_id(id, db)
