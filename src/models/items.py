from sqlalchemy import Column, Integer, String

from src.database import Base


class Items(Base):
    __tablename__: str = 'items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    user_id = Column(Integer)
