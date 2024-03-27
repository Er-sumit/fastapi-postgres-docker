# This file helps to keep api route entries outside main.py file, so that it won't get cluttered as we go up with number of api routes
from fastapi import APIRouter

from apis.v1 import route_user


api_router = APIRouter()
api_router.include_router(route_user.router,prefix="",tags=["users"])

# make sure we import this 'api_router' in the main.py file