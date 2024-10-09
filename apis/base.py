# This file helps to keep api route entries outside main.py file, so that it won't get cluttered as we go up with number of api routes
from fastapi import APIRouter

from apis.v1 import route_account
from apis.v1 import route_blog
from apis.v1 import route_login
from apis.v1 import route_metrics
from apis.v1 import route_txnmsgs
from apis.v1 import route_user


api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_blog.router, prefix="", tags=["blogs"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
api_router.include_router(route_account.router, prefix="", tags=["account"])
api_router.include_router(route_metrics.router, prefix="", tags=["metrics"])
api_router.include_router(route_txnmsgs.router, prefix="/txnmsgs", tags=["txnmsgs"])
# make sure we import this 'api_router' in the main.py file
