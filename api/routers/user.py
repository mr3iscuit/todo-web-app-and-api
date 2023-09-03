from typing import Annotated
from fastapi import APIRouter, HTTPException, Path, status
from pydantic import BaseModel
from starlette.exceptions import HTTPException

from tortoise.contrib.fastapi import register_tortoise
from api.models.user import User
from api.schemas.user import User_Pydantic, UserGet, UserPut

router = APIRouter(prefix="/api", tags=["Todo"])


class Status(BaseModel):
    message: str


@router.get("/users", response_model=list[User_Pydantic])
async def get_users():
    return await User_Pydantic.from_queryset(User.all())


@router.post("/users", response_model=User_Pydantic)
async def create_user(userIn: UserGet):
    user_obj = await User.create(**userIn.model_dump(exclude_unset=True))
    return await User_Pydantic.from_tortoise_orm(user_obj)


@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return await User_Pydantic.from_queryset_single(User.get(id=user_id))


@router.put("/users/{user_id}")
async def update_user(key: int, user: UserPut):
    exists = await User.filter(id=key).exists()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    await User.filter(id=key).update(**user.model_dump(exclude_unset=True))
    return await User_Pydantic.from_queryset_single(User.get(id=key))


@router.delete("/users/{id}")
async def delete_user(id: Annotated[int, Path(title="User ID")]):
    exists = await User.filter(id=id).exists()

    if not exists:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    await User.filter(id=id).delete()
    return f"Deleted user {id}"
