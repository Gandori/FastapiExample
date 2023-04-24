from fastapi import APIRouter

from src.crud.items import ItemsCrud
from src.crud.users import UsersCrud
from src.exeptions.items import (
    ItemCreatedSucess,
    ItemDeletedSucess,
    ItemNotFound,
    ItemUpdatedSucess,
)
from src.exeptions.users import UserNotFound
from src.schemas.items import ItemIn, ItemOut

router: APIRouter = APIRouter()
router.tags = ['Items']
crud: ItemsCrud = ItemsCrud()


@router.get('/items', response_model=list[ItemOut])
async def all():
    return await crud.all()


@router.post('/items/{user_id}')
async def new(user_id: int, item: ItemIn):
    try:
        await UsersCrud.exists(id=user_id)
        await crud.new(item=item, user_id=user_id)
    except UserNotFound:
        return UserNotFound().response()

    return ItemCreatedSucess().response()


@router.delete('/items/{id}')
async def delete(id: int):
    try:
        await crud.exists(id=id)
        await crud.delete(id=id)
    except ItemNotFound:
        return ItemNotFound().response()

    return ItemDeletedSucess().response()


@router.put('/items/{id}')
async def update(id: int, item: ItemIn):
    try:
        await crud.exists(id=id)
        await crud.update(id=id, item=item)
    except ItemNotFound:
        return ItemNotFound().response()

    return ItemUpdatedSucess().response()
