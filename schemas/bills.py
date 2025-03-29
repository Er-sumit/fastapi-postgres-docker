# scheme required for bills model and as used in repository/bills.py
from db.models.bills import Bills
from pydantic import BaseModel


class createBill(BaseModel):
    biller: str
    dueDate: str
    type: str
    billAmount: int
    paidAmount: int
    paidStatus: bool

class viewBill(BaseModel):
    id: int
    biller: str
    type: str
    billAmount: int
    paidAmount: int
    paidStatus: bool

class statusBill(BaseModel):
    status: str