from fastapi import APIRouter

from src.endpoints.example2 import crud
from src.schemas.example_2 import Example2

router: APIRouter = APIRouter()
router.tags = ['Example2']


@router.get('/example2', response_model=Example2)
async def example2():
    return crud.example(name='Example2')
