import datetime as dt
import uuid

from sqlalchemy.orm import Session

from core.config import log
from db.models.ipmessage import iPMessage
from db.models.ipmessage import txnMessage
from schemas.ipmessage import createIPMessage
from schemas.txn_msg_schema import txnMsgNewCreate


def create_new_ipmessage(imessage: createIPMessage, db: Session):
    this_doc = iPMessage(**imessage.dict())
    this_doc.id = str(uuid.uuid1())
    this_doc._number_ = "0"
    this_doc.usr_acted = False
    db.add(this_doc)
    db.commit()
    db.refresh(this_doc)
    return this_doc


def create_new_txnMsg():
    pass


def find_ipmessage():
    pass
