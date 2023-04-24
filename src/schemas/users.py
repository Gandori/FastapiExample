from pydantic import BaseModel


class UserIn(BaseModel):
    name: str


class UserOut(UserIn):
    id: int
