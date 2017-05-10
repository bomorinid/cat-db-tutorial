from sqlalchemy import ForeignKey, Column, Integer, String
from __init__ import Base


class CatHasFavoriteToy(Base):
    __tablename__ = 'cat_has_favorite_toy'
    cat_id = Column(Integer, ForeignKey('cat.id'), primary_key=True)
    cat_toy_id = Column(Integer, ForeignKey('cat_toy.id'), primary_key=True)


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat toy
    name = Column(String, unique=True)

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
