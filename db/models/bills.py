from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import relationship

from db.base_class import Base


class Bills(Base):
    id = Column(Integer, primary_key=True, index=True)
    biller = Column(String, nullable=False, index=True)
    dueDate = Column(String, default=False)
    type = Column(String, default=True)
    billAmount = Column(Integer)
    paidAmount = Column(Integer, nullable=True, default=None)
    paidStatus = Column(Boolean)
