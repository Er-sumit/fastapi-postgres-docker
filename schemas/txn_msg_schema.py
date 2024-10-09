from datetime import date
from typing import Optional

from pydantic import BaseModel
from pydantic import root_validator


class txnMsgNewCreate(BaseModel):
    sender: str
    text: str
    timestamp: str
    type: str
    receiver: str
    _number_: str
    amount: int
    accounts_info: str
    to_id: Optional[str] = ""
