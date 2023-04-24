from fastapi import APIRouter

from src.crud.users import UsersCrud
from src.exeptions.users import (
    UserCreatedSucess,
    UserDeletedSucess,
    UserNotFound,
    UserUpdatedSucess,
)
from src.schemas.users import UserIn, UserOut

router: APIRouter = APIRouter()
router.tags = ['Users']
crud: UsersCrud = UsersCrud()


@router.get('/users', response_model=list[UserOut])
async def all():
    return await crud.all()


@router.post('/users')
async def new(user: UserIn):
    await crud.new(user=user)
    return UserCreatedSucess().response()


@router.delete('/users/{id}')
async def delete(id: int):
    try:
        await crud.exists(id=id)
        await crud.delete(id=id)
    except UserNotFound:
        return UserNotFound().response()

    return UserDeletedSucess().response()


@router.put('/users/{id}')
async def update(id: int, user: UserIn):
    try:
        await crud.exists(id=id)
        await crud.update(id=id, user=user)
    except UserNotFound:
        return UserNotFound().response()

    return UserUpdatedSucess().response()
