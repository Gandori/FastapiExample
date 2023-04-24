from src.database import db
from src.models.users import Users
from src.schemas.users import UserIn, UserOut


class Crud:
    @staticmethod
    async def all() -> list[UserOut]:
        return await db.select_all(table=Users, order=Users.id)

    @staticmethod
    async def new(user: UserIn) -> None:
        await db.add(row=Users(**user.dict()))
