from fastapi import APIRouter

from src.crud.users import UsersCrud
from src.exeptions.users import (
    UserCreatedSucess,
    UserDeletedSucess,
    UserNotFound,
    UserUpdatedSucess,
)
from src.schemas.items import ItemOut
from src.schemas.users import UserIn, UserOut

router: APIRouter = APIRouter()
router.tags = ['Users']
crud: UsersCrud = UsersCrud()


@router.get('/users', response_model=list[UserOut])
async def all():
    Users: list[UserOut] = []
    for user in await crud.all():
        items: list[ItemOut] = await crud.get_items(user_id=user.id)
        Users.append(UserOut(**user.__dict__, items=items))
    return Users


@router.post('/users')
async def new(user: UserIn):
    await crud.new(user=user)
    return UserCreatedSucess().response()


@router.delete('/users/{id}')
async def delete(id: int):
    try:
        await crud.exists(id=id)
        await crud.delete_items(user_id=id)
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
