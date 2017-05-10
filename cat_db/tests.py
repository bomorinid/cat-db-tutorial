from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base
from unittest import TestCase
from models import Cat, CatToy


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

    def test_add_cat_toy_function(self):
        # basic things about cat toys - they have names

        crinkle_tunnel = CatToy(name='crinkle tunnel')
