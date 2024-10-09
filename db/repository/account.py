from sqlalchemy.orm import Session

from core.config import log
from db.models.account import Account
from schemas.account import CreateAccount
from schemas.account import ShowAccount
from schemas.account import UpdateAccount
from schemas.account import UpdateAccountState


def create_new_account(account: CreateAccount, db: Session):
    this_account = Account(**account.dict())
    db.add(this_account)
    db.commit()
    db.refresh(this_account)
    return this_account


def retreive_account(id: int, db: Session):
    account = db.query(Account).filter(Account.id == id).first()
    return account


def list_accounts(db: Session):
    accounts = db.query(Account).filter(Account.active_flag == 1).all()
    log.info(f"found {len(accounts)} account to list API")
    return accounts


def update_account_state(id: int, state: int, db: Session):
    account_in_db = db.query(Account).filter(Account.id == id).first()
    if not account_in_db:
        return None
    account_in_db.active_flag = state
    db.add(account_in_db)
    db.commit()
    return account_in_db


def update_account(id: int, account: UpdateAccount, db: Session):
    account_in_db = db.query(Account).filter(Account.id == id).first()
    if not account_in_db:
        return None
    account_in_db.title = account.title
    account_in_db.type = account.type
    account_in_db.bank_desc = account.bank_desc
    account_in_db.billed_due = account.billed_due
    account_in_db.unbilled_due = account.unbilled_due
    account_in_db.total_due = account.total_due
    account_in_db.billing_date = account.billing_date
    account_in_db.available_bal = account.available_bal

    db.add(account_in_db)
    db.commit()
    return account_in_db


def delete_account(id: int, db: Session):
    account_in_db = db.query(Account).filter(Account.id == id).first()
    if not account_in_db:
        return {"error": f"Could not find account with id {id}"}
    account_in_db.active_flag = 0
    db.add(account_in_db)
    db.commit()
    return {"msg": f"archieved blog with id {id}"}
