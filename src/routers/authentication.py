from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas, database
from ..repository import authentication


router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    return authentication.login(request, db)
