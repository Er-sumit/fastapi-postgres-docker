# This handles the responsibility of creating a new user and returning it.

from sqlalchemy.orm import Session
from db.repository.user import create_new_user
from schemas.user import UserCreate

from datetime import datetime
dt_string = datetime.now().strftime("%d%m%Y%H%M%S")
myemail = f"testusr{dt_string}@nofoobar.com"

def create_random_user(db: Session):
    user = UserCreate(email=myemail,password="Hello!")
    user = create_new_user(user=user, db=db)
    return user