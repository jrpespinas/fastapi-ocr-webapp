from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from .. import schemas, models
from ..security import Hashing


def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials!"
        )

    # if not Hashing.verify_password(user.password, request.password):
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password!"
    #     )

    return user
