from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from business.txnmsg_main import txnmsg_main
from business.txnmsgs_refresh import txnmsgs_refresh_getapi
from core.config import log
from db.repository.ipmessage import create_new_ipmessage
from db.session import get_db
from schemas.ipmessage import createIPMessage

router = APIRouter()


@router.get("/test_new_msgs/")
def get_txnmsgs(db: Session = Depends(get_db)):
    # value = total_assets(db)
    # if not value:
    #     value = 0
    data = txnmsgs_refresh_getapi(db)
    return {"m_transactions": data}


@router.post("syncdb", status_code=status.HTTP_200_OK)
async def sync_imsgdb(db: Session = Depends(get_db)):
    txnmsg_main(db=db)
    return {"status": "Ok"}


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def post_account(imessage: createIPMessage, db: Session = Depends(get_db)):
    # log.info("calling to create new imessage", imessage)
    imsg = create_new_ipmessage(imessage, db=db)
    log.info(imsg)
    return {"imsg": "ok"}
