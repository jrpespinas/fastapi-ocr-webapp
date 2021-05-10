from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from .. import schemas, models
from ..security import Hashing
from . import token


def login(request: schemas.Login, db: Session):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials!"
        )

    if not Hashing.verify_password(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password!"
        )

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
