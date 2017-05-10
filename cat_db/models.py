from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from __init__ import Base


class CatHasFavoriteToy(Base):
    __tablename__ = 'cat_has_favorite_toy'
    cat_id = Column(Integer, ForeignKey('cat.id'), primary_key=True)
    cat_toy_id = Column(Integer, ForeignKey('cat_toy.id'), primary_key=True)
    cat = relationship('Cat', back_populates='favorite_toy_associations')


class Cat(Base):
    __tablename__ = 'cat'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat
    name = Column(String)
    age = Column(Integer)
    coloring = Column(String)
    gender = Column(String)

    # relationship manager linking Cat to CatToyAssociation
    # allows you to call Cat().favorite_toy_associations and get back all
    # CatHasFavoriteToy objects linked to that Cat
    favorite_toy_associations = relationship("CatHasFavoriteToy", back_populates='cat')

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat toy
    name = Column(String, unique=True)

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
