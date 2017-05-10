from sqlalchemy import Column, Integer, String
from __init__ import Base


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat toy
    name = Column(String, unique=True)
