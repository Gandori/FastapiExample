from fastapi import APIRouter

from src.crud.users import Crud
from src.exeptions.users import CreatedSucess, DeletedSucess, NotFound
from src.schemas.users import UserIn, UserOut

router: APIRouter = APIRouter()
router.tags = ['Users']


@router.get('/users', response_model=list[UserOut])
async def all():
    return await Crud.all()


@router.post('/users')
async def new(user: UserIn):
    await Crud.new(user=user)
    return CreatedSucess().response()


@router.delete('/users/{id}')
async def delete(id: int):
    try:
        await Crud.delete(id=id)
    except NotFound:
        return NotFound().response()

    return DeletedSucess().response()
