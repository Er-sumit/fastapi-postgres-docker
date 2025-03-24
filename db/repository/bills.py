# method to create new bill in models.bills.py
from sqlalchemy.orm import Session

from db.models.bills import Bills
from schemas.bills import createBill

def create_new_bill(bill: createBill, db: Session):
    this_doc = Bills(**bill.dict())
    db.add(this_doc)
    db.commit()
    db.refresh(this_doc)
    return this_doc

# method to get all bills in models.bills.py
def get_all_bills(db: Session):
    all_bills_data = db.query(Bills).all()
    return all_bills_data

# method to get bill by id in models.bills.py
def get_bill_by_id(id: str, db: Session):
    return db.query(Bills).filter(Bills.id == id).first()

# method to update bill by id in models.bills.py
def update_bill_by_id(id: str, bill: createBill, db: Session):
    this_doc = db.query(Bills).filter(Bills.id == id).first()
    this_doc.biller = bill.biller
    this_doc.dueDate = bill.dueDate
    this_doc.type = bill.type
    this_doc.billAmount = bill.billAmount
    this_doc.paidAmount = bill.paidAmount
    this_doc.paidStatus = bill.paidStatus
    db.commit()
    db.refresh(this_doc)
    return this_doc

# method to delete bill by id in models.bills.py
def delete_bill_by_id(id: str, db: Session):
    this_doc = db.query(Bills).filter(Bills.id == id).first()
    db.delete(this_doc)
    db.commit()
    return this_doc

# method to get bills by biller in models.bills.py
def get_bill_by_biller(biller: str, db: Session):
    return db.query(Bills).filter(Bills.biller == biller).all()

# method to get bills by due date in
# models.bills.py
def get_bill_by_due_date(dueDate: str, db: Session):
    return db.query(Bills).filter(Bills.dueDate == dueDate).all()

# method to get bills by type in models.bills.py
def get_bill_by_type(type: str, db: Session):
    return db.query(Bills).filter(Bills.type == type).all()
