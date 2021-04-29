from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..repository import blog


router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/", response_model=List[schemas.ShowBlog])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_blog_by_id(id: int, db: Session = Depends(database.get_db)):
    return blog.get_by_id(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available!",
        )
    else:
        blog.update({"title": request.title, "body": request.body})

    db.commit()
    return {"message": "Updated"}


@router.delete("/{id}")
def destroy(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available!",
        )
    else:
        blog.delete(synchronize_session=False)

    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
