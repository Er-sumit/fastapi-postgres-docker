from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Date  # Import Date type
from sqlalchemy.orm import relationship

from db.base_class import Base


class Bills(Base):
    id = Column(Integer, primary_key=True, index=True)
    biller = Column(String, nullable=False, index=True)
    dueDate = Column(Date)  # Changed from String to Date
    type = Column(String, default=True)
    billAmount = Column(Integer)
    paidAmount = Column(Integer, nullable=True, default=None)
    outstandingAmount = Column(Integer, nullable=True, default=None)
    paidStatus = Column(Boolean)