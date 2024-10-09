"""
To mark break point for processed messages
"""
from datetime import datetime
from unittest.main import MODULE_EXAMPLES

from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from db.base_class import Base


class regMsgs(Base):
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    ipmessage = Column(String)
