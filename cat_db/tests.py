from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from __init__ import Base
from unittest import TestCase


class BaseTest(TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        Base.metadata.create_all(bind=self.engine)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.engine)
