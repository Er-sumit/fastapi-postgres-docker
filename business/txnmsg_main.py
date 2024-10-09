from fastapi import Depends
from sqlalchemy.orm import Session

from business.definitions.iMessages import iMessages
from core.config import log
from db.repository.ipmessage import create_new_ipmessage
from db.repository.ipmessage import find_ipmessage
from db.session import get_db


def sync_imessages_db(db, imsg):
    """sync imessages dataset with given imsg & returns status_code"""
    if not find_ipmessage(*imsg):
        create_new_ipmessage(*imsg)


def txnmsg_main(db):
    """Process imessages into application"""
    txn_messages = iMessages.get_messages(iMessages())
    # check if txn_msg already in db and add if not available
    [sync_imessages_db(db, imsg=imsg) for imsg in txn_messages]
    # post unprocessed imessages
    return {"status": "Success"}


if __name__ == "__main__":
    db: Session = Depends(get_db)
    txnmsg_main(db=db)
