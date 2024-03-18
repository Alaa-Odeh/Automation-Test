import unittest
from decimal import Decimal
from models import Product, engine, Base
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

class TestProductOperations(unittest.TestCase):

    def setUp(self):
        Base.metadata.create_all(engine)
        new_product = Product(name='Sample Product', price=326)
        session.add(new_product)
        session.commit()


    def test_adding_product(self):
        product = session.query(Product).first()
        self.assertIsNotNone(product)
        self.assertEqual(product.name, 'Sample Product')

    def test_reading_product(self):
        product = session.query(Product).first()
        self.assertEqual(product.name, 'Sample Product')

    def test_updating_product(self):
        product = session.query(Product).first()
        product.price = 543.21
        session.commit()
        updated_product = session.query(Product).first()
        self.assertEqual(updated_product.price, Decimal('543.21'))

    def test_deleting_product(self):
        product = session.query(Product).first()
        session.delete(product)
        session.commit()
        product_count = session.query(Product).count()
        self.assertEqual(product_count, 0)

    def tearDown(self):
        Base.metadata.drop_all(engine)
        session.close()

# Run the tests
if __name__ == '__main__':
    unittest.main()