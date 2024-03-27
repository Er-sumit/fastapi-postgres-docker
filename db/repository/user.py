from sqlalchemy.orm import Session

from schemas.user import UserCreate # validations
from db.models.user import User
from core.hashing import Hasher
from core.config import log


def create_new_user(user:UserCreate,db:Session):
    user = User(
        email = user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

'''
In function create_new_user, user: UserCreate is annotating that the user parameter is expected to be an instance of the UserCreate class, helping to convey the expected type of data being passed to the function.
This practice is part of Python's optional type hinting feature introduced in PEP 484, which allows developers to add type hints to their code for improved clarity, documentation, and potential static type analysis by tools like MyPy.
'''

def retrieve_user(id: int, db: Session):
    try:
        user = db.query(User.id, User.email).filter(User.id == id)
        log.info(type(user))
        log.info(dir(user))
        log.info(user)
    except Exception as e:  
        log.error(e)
    return user

