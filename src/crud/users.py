from src.database import db
from src.exeptions.users import NotFound
from src.models.users import Users
from src.schemas.users import UserIn, UserOut


class Crud:
    @staticmethod
    async def all() -> list[UserOut]:
        return await db.select_all(table=Users, order=Users.id)

    @staticmethod
    async def new(user: UserIn) -> None:
        await db.add(row=Users(**user.dict()))

    @staticmethod
    async def exists(id: int) -> None:
        if not await db.select_where(table=Users, where=Users.id == id):
            raise NotFound

    @staticmethod
    async def delete(id: int) -> None:
        await db.delete(table=Users, where=Users.id == id)
