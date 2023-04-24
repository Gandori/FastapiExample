from fastapi import APIRouter

from src.crud.example_2 import Example2Grud
from src.schemas.example_2 import Example2

router: APIRouter = APIRouter()
router.tags = ['Example2']

crud = Example2Grud()


@router.get('/example2', response_model=Example2)
async def example2():
    return crud.example(name='Example2')
