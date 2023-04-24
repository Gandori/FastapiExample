from src.database import db
from src.exeptions.users import UserNotFound
from src.models.users import Users
from src.schemas.users import UserIn, UserOut


class UsersCrud:
    @staticmethod
    async def all() -> list[UserOut]:
        return await db.select_all(table=Users, order=Users.id)

    @staticmethod
    async def new(user: UserIn) -> None:
        await db.add(row=Users(**user.dict()))

    @staticmethod
    async def exists(id: int) -> None:
        if not await db.select_where(table=Users, where=Users.id == id):
            raise UserNotFound

    @staticmethod
    async def delete(id: int) -> None:
        await db.delete(table=Users, where=Users.id == id)

    @staticmethod
    async def update(id: int, user: UserIn) -> None:
        await db.update_where(table=Users, values=user.dict(), where=Users.id == id)
