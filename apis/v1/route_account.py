from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session

from core.config import log
from db.repository.account import create_new_account
from db.repository.account import delete_account
from db.repository.account import list_accounts
from db.repository.account import retreive_account
from db.repository.account import update_account
from db.repository.account import update_account_state
from db.session import get_db
from schemas.account import CreateAccount
from schemas.account import ShowAccount
from schemas.account import UpdateAccount

router = APIRouter()


@router.post(
    "/account", response_model=ShowAccount, status_code=status.HTTP_201_CREATED
)
async def post_account(account: CreateAccount, db: Session = Depends(get_db)):
    account = create_new_account(account=account, db=db)
    return account


@router.get("/account/{id}", response_model=ShowAccount)
def get_account(id: int, db: Session = Depends(get_db)):
    account = retreive_account(id=id, db=db)
    if not account:
        raise HTTPException(
            detail=f"account with ID {id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return account


@router.get("/accounts", response_model=List[ShowAccount])
def get_all_accounts(db: Session = Depends(get_db)):
    log.debug("get all accounts")
    accounts = list_accounts(db=db)
    return accounts


@router.put("/account/{id}/activation/{state}", response_model=ShowAccount)
def update_an_account_state(id: int, state: int, db: Session = Depends(get_db)):
    account = update_account_state(id=id, state=state, db=db)
    if not account:
        raise HTTPException(
            detail=f"account with id {id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return account


@router.put("/account/{id}", response_model=ShowAccount)
def update_an_account(id: int, account: UpdateAccount, db: Session = Depends(get_db)):
    account = update_account(id=id, account=account, db=db)
    if not account:
        raise HTTPException(
            detail=f"account with id {id} does not exist",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return account


@router.delete("/account/delete/{id}")
def delete_an_account(id: int, db: Session = Depends(get_db)):
    message = delete_account(id=id, db=db)
    if message.get("error"):
        raise HTTPException(
            detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST
        )
    return {"msg": f"Successfully deleted account with id {id}"}
