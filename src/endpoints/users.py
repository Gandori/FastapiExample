from fastapi import APIRouter

from src.crud.users import Crud
from src.exeptions.users import (
    UserCreatedSucess,
    UserDeletedSucess,
    UserNotFound,
    UserUpdatedSucess,
)
from src.schemas.users import UserIn, UserOut

router: APIRouter = APIRouter()
router.tags = ['Users']


@router.get('/users', response_model=list[UserOut])
async def all():
    return await Crud.all()


@router.post('/users')
async def new(user: UserIn):
    await Crud.new(user=user)
    return UserCreatedSucess().response()


@router.delete('/users/{id}')
async def delete(id: int):
    try:
        await Crud.exists(id=id)
        await Crud.delete(id=id)
    except UserNotFound:
        return UserNotFound().response()

    return UserDeletedSucess().response()


@router.put('/users/{id}')
async def update(id: int, user: UserIn):
    try:
        await Crud.exists(id=id)
        await Crud.update(id=id, user=user)
    except UserNotFound:
        return UserNotFound().response()

    return UserUpdatedSucess().response()
