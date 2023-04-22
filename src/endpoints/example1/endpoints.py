from fastapi import APIRouter

from src.endpoints.example1 import crud
from src.schemas.example_1 import Example1

router: APIRouter = APIRouter()
router.tags = ['Example1']


@router.get('/example1', response_model=Example1)
async def example1():
    return crud.example(name='Example1')
