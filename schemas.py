from pydantic import BaseModel
from typing import List


class User(BaseModel):
    name : str
    email : str
    password : str

class Created_User(BaseModel):
    name : str
    email: str

    
class Show_User(BaseModel):
    #id:int
    name :str
    email:str

    # class Config():
    #     orm_mode = True

class Login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str    