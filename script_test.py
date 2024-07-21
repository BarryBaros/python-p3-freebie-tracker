import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Company, Dev, Freebie

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///lib/freebies.db', echo=True)
        Base.metadata.create_all(cls.engine)
        cls.Session = sessionmaker(bind=cls.engine)
        cls.session = cls.Session()

    def setUp(self):
        self.session.query(Freebie).delete()
        self.session.query(Dev).delete()
        self.session.query(Company).delete()
        self.session.commit()

    def tearDown(self):
        self.session.query(Freebie).delete()
        self.session.query(Dev).delete()
        self.session.query(Company).delete()
        self.session.commit()

    def test_add_company_and_dev(self):
        company = Company(name="Tech Corp", founding_year=2000)
        dev = Dev(name="Tim")

        self.session.add(company)
        self.session.add(dev)
        self.session.commit()

        self.assertEqual(len(self.session.query(Company).all()), 1)
        self.assertEqual(len(self.session.query(Dev).all()), 1)
        self.assertEqual(self.session.query(Company).first().name, "Tech Corp")
        self.assertEqual(self.session.query(Dev).first().name, "Tim")

    def test_add_freebie(self):
        company = Company(name="Tech Corp", founding_year=2000)
        dev = Dev(name="Tim")
        freebie = Freebie(item_name="T-Shirt", value=10, dev=dev, company=company)

        self.session.add(company)
        self.session.add(dev)
        self.session.add(freebie)
        self.session.commit()

        retrieved_freebie = self.session.query(Freebie).first()
        self.assertEqual(retrieved_freebie.item_name, "T-Shirt")
        self.assertEqual(retrieved_freebie.dev.name, "Tim")
        self.assertEqual(retrieved_freebie.company.name, "Tech Corp")

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(cls.engine)

if __name__ == '__main__':
    unittest.main()
