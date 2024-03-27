# A schema is used to validate the data we receive as well as to reformat the data that we want to send to the client/browser.
# https://www.fastapitutorial.com/blog/pydantic-schemas-in-fastapi/
from pydantic import BaseModel,EmailStr, Field


# properties required during user creation, We are inheriting BaseModel from pydantic. It empowers fastapi to suggest validation errors to users.
class UserCreate(BaseModel):
    email : EmailStr
    password : str = Field(..., min_length=4)