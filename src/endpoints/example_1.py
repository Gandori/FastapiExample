from fastapi import APIRouter

from src.crud.example_1 import Example1Grud
from src.schemas.example_1 import Example1

router: APIRouter = APIRouter()
router.tags = ['Example1']

crud = Example1Grud()


@router.get('/example1', response_model=Example1)
async def example1():
    return crud.example(name='Example1')
