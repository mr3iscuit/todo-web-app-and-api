from typing import Annotated
from fastapi import APIRouter, Body, Path

from api.models.todo import Todo
from api.schemas.todo import PostTodo, PutTodo

router = APIRouter(prefix="", tags=["Todo"])

@router.get("/todos/")
async def get_todo():
    return "Not Implemented"

@router.post("/todos/")
async def post_todo(
    body: Annotated[PostTodo, Body()]
):
    return "Not Implemented"

@router.put("/todos/{id}")
async def put_todo(
        key: int,
        body: Annotated[PutTodo, Body()]
):
    return "Not Implemented"

@router.delete("/todos/{id}")
async def delete_todo(key: Annotated[int, Path()]):
    return "Not Implemented"

