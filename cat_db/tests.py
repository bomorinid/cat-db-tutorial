from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base
from unittest import TestCase
from models import Cat, CatToy, CatHasFavoriteToy


class BaseTest(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.create_all(bind=self.engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)


class ModelTestCase(BaseTest):

    def test_add_cat_function(self):
        # some basic things about cats - they have names, ages, gender,
        # and coloring:

        gwen = Cat(
            name='Gwen',
            age=19,
            coloring='tuxedo',
            gender='female'
        )
        self.session.add(gwen)

    def test_add_cat_toy_function(self):
        # basic things about cat toys - they have names

        crinkle_tunnel = CatToy(name='crinkle tunnel')
        self.session.add(crinkle_tunnel)


class RelationshipTestCase(BaseTest):
    def test_add_cat_favorite_toy(self):
        gwen = Cat(
            name='Gwen',
            age=19,
            coloring='tuxedo',
            gender='female'
        )
        self.session.add(gwen)

        crinkle_tunnel = CatToy(name='crinkle tunnel')
        self.session.add(crinkle_tunnel)

        fav_toy = CatHasFavoriteToy(
            cat_id=gwen.id,
            cat_toy_id=crinkle_tunnel.id
        )
        self.session.add(fav_toy)

    def test_cat_cat_toy_relationship(self):
        # establish a cat
        gwen = Cat(
            name='Gwen',
            age=19,
            coloring='tuxedo',
            gender='female'
        )
        self.session.add(gwen)
        self.session.flush()

        # establish some toys she can play with
        available_toys = [
            'owl plush',
            'feather boa',
            'crinkle tunnel',
            'squeaky mouse'
        ]

        for toy in available_toys:
            toy = CatToy(name=toy)
            self.session.add(toy)
        self.session.flush()

        # establish which ones she likes to play with best
        gwens_fav_toys = ['owl plush', 'feather boa']

        for toy_name in gwens_fav_toys:
            fav_toy = self.session.query(CatToy).filter(CatToy.name == toy_name).one()
            fav_toy_association = CatHasFavoriteToy(cat_id=gwen.id, cat_toy_id=fav_toy.id)
            self.session.add(fav_toy_association)
        self.session.flush()
        # the CatToy objects related to the CatHasFavoriteToys
        # we just made for Gwen should now live in
        # gwen.toys
        # is there the correct amount?
        self.assertEqual(len(gwens_fav_toys), len(gwen.toys))

        # are they the correct ones?
        for cat_toy in gwen.toys:
            self.assertTrue(cat_toy.name in gwens_fav_toys)
