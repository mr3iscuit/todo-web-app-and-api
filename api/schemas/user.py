from typing import Annotated
from pydantic import BaseModel, Field

from api.models.user import User
from tortoise.contrib.pydantic.creator import pydantic_model_creator

User_Pydantic = pydantic_model_creator(User, name="User")

class UserGet(BaseModel):
    username: Annotated[str, Field(max_length=100)]
    name: Annotated[str, Field(max_length=100)]
    surname: Annotated[str, Field(max_length=100)]
    category: Annotated[str, Field(max_length=100)]

class UserPut(BaseModel):
    username: Annotated[str|None, Field(max_length=100)] = None
    name: Annotated[str|None, Field(max_length=100)] = None
    surname: Annotated[str|None, Field(max_length=100)] = None
    category: Annotated[str|None, Field(max_length=100)] = None
