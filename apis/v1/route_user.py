from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.user import UserCreate
from db.session import get_db
from db.repository.user import create_new_user

router = APIRouter()


@router.post("/")
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    '''
    This is the definition of the create_user function. It takes two parameters:

    user: This parameter represents the data for creating a new user. It's expected to be an instance of the UserCreate Pydantic model. The : UserCreate part is a type hint, specifying the expected type of the user parameter.
    db: This parameter represents a database session. It's obtained using the Depends(get_db) syntax, which means that FastAPI will call the get_db function to get the database session when this endpoint is called. This function is part of the dependency injection system in FastAPI.
    '''
    user = create_new_user(user=user,db=db)
    return user 

