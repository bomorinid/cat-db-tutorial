from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy
from __init__ import Base


class CatHasFavoriteToy(Base):
    __tablename__ = 'cat_has_favorite_toy'
    cat_id = Column(Integer, ForeignKey('cat.id'), primary_key=True)
    cat_toy_id = Column(Integer, ForeignKey('cat_toy.id'), primary_key=True)
    # relationship manager linking cat toys to their cat associations
    cat_toy = relationship("CatToy", back_populates="favorite_toy_associations")

    # relationship manager linking cats to their cat toy associations
    cat = relationship("Cat", back_populates="favorite_toy_associations")


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

    # create a proxy from Cat().toys to CatToy() for each CatToyAssociation
    # linked to this Cat
    toys = association_proxy('favorite_toy_associations', 'cat_toy')

    def __repr__(self):
        return "<Cat(%s, %s, %s)>" % (self.name, self.age, self.coloring)


class CatToy(Base):
    __tablename__ = 'cat_toy'

    id = Column(Integer, primary_key=True, autoincrement=True)

    # properties of a cat toy
    name = Column(String, unique=True)

    # relationship manager linking CatToy to CatToyAssociation
    # allows you to call CatToy().favorite_toy_associations and get back all
    # CatHasFavoriteToy objects linked to that CatToy
    favorite_toy_associations = relationship("CatHasFavoriteToy", back_populates='cat_toy')

    def __repr__(self):
        return "<CatToy('%s')>" % self.name
