from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from core.config import log
from db.repository.user import create_new_user
from db.repository.user import retrieve_user
from db.session import get_db
from schemas.user import ShowUser
from schemas.user import UserCreate

router = APIRouter()


@router.post("/user", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    This is the definition of the create_user function. It takes two parameters:

    user: This parameter represents the data for creating a new user. It's expected to be an instance of the UserCreate Pydantic model. The : UserCreate part is a type hint, specifying the expected type of the user parameter.
    db: This parameter represents a database session. It's obtained using the Depends(get_db) syntax, which means that FastAPI will call the get_db function to get the database session when this endpoint is called. This function is part of the dependency injection system in FastAPI.
    """
    user = create_new_user(user=user, db=db)
    log.info(f"New user created? => {True if user else False}")
    if user:
        log.info(f"user={user.email} and status={status.HTTP_201_CREATED}")
    else:
        raise HTTPException(
            detail="Failed to create user", status_code=status.HTTP_400_BAD_REQUEST
        )
    return user


@router.get("/user/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    log.info(f"calling retrieve user for id={id}")
    try:
        user = retrieve_user(id=id, db=db)
    except Exception as e:
        log.error(e)
        user = None
    if not user:
        raise HTTPException(
            detail=f"user with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return user
