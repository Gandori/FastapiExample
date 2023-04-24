from fastapi import APIRouter

from src.crud.users import Crud
from src.schemas.users import UserIn, UserOut

router: APIRouter = APIRouter()
router.tags = ['Users']


@router.get('/users', response_model=list[UserOut])
async def all():
    return await Crud.all()


@router.post('/users')
async def new(user: UserIn):
    await Crud.new(user=user)
    return user
