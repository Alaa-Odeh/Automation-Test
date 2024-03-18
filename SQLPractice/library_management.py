from datetime import  date
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,declarative_base


engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(Date)

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}', publication_date='{self.publication_date}')>"


# Create all tables in the engine
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add book data to the session
book1 = Book(title='Book Title 1', author='Author 1', publication_date=date(2024, 3, 17))
book2 = Book(title='Book Title 2', author='Author 2', publication_date=date(2024, 3, 18))

session.add(book1)
session.add(book2)

session.commit()

all_books = session.query(Book).all()
for book in all_books:
    print(book)

# Implement search by author
author_search = session.query(Book).filter(Book.author == 'Author 1').all()
for book in author_search:
    print(book)

# Close the session
session.close()