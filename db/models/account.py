from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.orm import relationship

from db.base_class import Base


class Account(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    type = Column(String, nullable=False)
    bank_desc = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.now)
    billed_due = Column(Integer, default=0)
    due_date = Column(Integer, nullable=True)
    unbilled_due = Column(Integer, default=0)
    total_due = Column(Integer, default=0)
    billing_date = Column(Integer, default=0)
    available_bal = Column(Integer, default=0)
    active_flag = Column(Integer, default=0)
    emi_amount = Column(Integer, default=None, nullable=True)
    emi_due_count = Column(Integer, default=None, nullable=True)
