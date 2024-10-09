from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import root_validator


class CreateAccount(BaseModel):
    title: str
    type: str
    bank_desc: Optional[str] = None
    billed_due: int
    unbilled_due: int
    total_due: int
    due_date: int
    billing_date: int
    available_bal: int
    emi_amount: int
    emi_due_count: int


class ShowAccount(BaseModel):
    id: int
    title: str
    type: str
    bank_desc: Optional[str] = None
    billed_due: int
    unbilled_due: int
    total_due: int
    due_date: int
    billing_date: int
    available_bal: int
    emi_amount: int
    emi_due_count: int

    class Config:
        orm_mode = True


class UpdateAccount(CreateAccount):
    pass


class UpdateAccountState(BaseModel):
    id: int
    title: str
    type: str
