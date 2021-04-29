from sqlalchemy.orm import Session
from .. import models

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def get_by_id(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Blog with the id {id} is not available!",
        )
    return blog