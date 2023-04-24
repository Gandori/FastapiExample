from pydantic import BaseModel

from src.schemas.items import ItemOut


class UserIn(BaseModel):
    name: str


class UserOut(UserIn):
    id: int
    items: list[ItemOut]
