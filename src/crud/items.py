from src.database import db
from src.exeptions.items import ItemNotFound
from src.models.items import Items
from src.schemas.items import ItemDB, ItemIn, ItemOut


class ItemsCrud:
    @staticmethod
    async def all() -> list[ItemOut]:
        return await db.select_all(table=Items, order=Items.id)

    @staticmethod
    async def new(item: ItemIn, user_id) -> None:
        item_db: ItemDB = ItemDB(**item.dict(), user_id=user_id)
        await db.add(row=Items(**item_db.dict()))

    @staticmethod
    async def exists(id: int) -> None:
        if not await db.select_where(table=Items, where=Items.id == id):
            raise ItemNotFound

    @staticmethod
    async def delete(id: int) -> None:
        await db.delete(table=Items, where=Items.id == id)

    @staticmethod
    async def update(id: int, item: ItemIn) -> None:
        await db.update_where(table=Items, values=item.dict(), where=Items.id == id)
