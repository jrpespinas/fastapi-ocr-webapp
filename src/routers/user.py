"""
This program is composed of the endpoints for the `Users` module.
"""
from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, database, models
from ..security import Hashing
from ..repository import user

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create_user(request, db)


@router.get("/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get_user_by_id(id, db)
