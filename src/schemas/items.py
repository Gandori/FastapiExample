from pydantic import BaseModel


class Item(BaseModel):
    user_id: int


class ItemIn(BaseModel):
    name: str
    description: str


class ItemOut(Item, ItemIn):
    id: int


class ItemDB(Item, ItemIn):
    pass
