from typing import Annotated
from fastapi import APIRouter, Body, HTTPException, Path, status

from api.models.todo import Todo
from api.schemas.todo import GetTodo, PostTodo, PutTodo

router = APIRouter(prefix="/api", tags=["Todo"])


@router.get("/todos")
async def get_todos():
    return await GetTodo.from_queryset(Todo.all())


@router.post("/todos")
async def post_todo(body: Annotated[PostTodo, Body()]):
    todo = await Todo.create(**body.model_dump(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(todo)


@router.get("/todo/{id}")
async def get_todo(id: int):
    return await GetTodo.from_queryset_single(Todo.get(id=id))


@router.put("/todos/{id}")
async def put_todo(key: int, body: Annotated[PutTodo, Body()]):
    exists = await Todo.filter(id=key).exists()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    await Todo.filter(id=key).update(**body.model_dump(exclude_unset=True))
    return await GetTodo.from_queryset_single(Todo.get(id=key))


@router.delete("/todos/{id}")
async def delete_todo(id: Annotated[int, Path(title="Todo ID")]):
    exists = await Todo.filter(id=id).exists()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    await Todo.filter(id=id).delete()
    return f"Deleted todo {id}"
