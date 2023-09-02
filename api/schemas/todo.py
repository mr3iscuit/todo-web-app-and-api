from typing import Annotated
from pydantic import BaseModel, Field
from tortoise.contrib.pydantic.creator import pydantic_model_creator

from api.models.todo import Todo

GetTodo = pydantic_model_creator(Todo, name="Todo")

class PostTodo(BaseModel):
    title: Annotated[str, Field(max_length=100)]
    completed: Annotated[bool, Field()]

class PutTodo(BaseModel):
    title: Annotated[str|None, Field(max_length=100)]
    completed: Annotated[bool|None, Field()]
