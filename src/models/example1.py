from sqlalchemy import Column, Integer, String

from src.database import Base


class Examples1(Base):
    __tablename__: str = 'examples1'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
