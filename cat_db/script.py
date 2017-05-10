from __init__ import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Cat, CatToy, CatHasFavoriteToy

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

gwen = Cat(
    name='Gwen',
    age=19,
    coloring='tuxedo',
    gender='female'
)
session.add(gwen)
session.flush()

available_toys = ['owl plush', 'feather boa', 'crinkle tunnel', 'squeaky mouse']
for toy in available_toys:
    toy = CatToy(name=toy)
    session.add(toy)
session.flush()

gwens_fav_toys = ['owl plush', 'feather boa']

for toy_name in gwens_fav_toys:
    fav_toy = session.query(CatToy).filter(CatToy.name == toy_name).one()
    fav_toy_association = CatHasFavoriteToy(cat_id=gwen.id, cat_toy_id=fav_toy.id)
    session.add(fav_toy_association)

gwens_toy_associations = session.query(CatHasFavoriteToy).filter(CatHasFavoriteToy.cat_id ==  gwen.id).all()
gwens_toys = session.query(CatToy).filter(CatToy.id.in_([ta.cat_toy_id for ta in gwens_toy_associations])).all()
print gwens_toys
