from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)

    def __repr__(self):
        return f"<Product(name='{self.name}', price={self.price})>"

Base.metadata.create_all(engine)