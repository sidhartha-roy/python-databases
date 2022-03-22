from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://postgres:password@localhost:5432/books')
Base = declarative_base()

class Author(Base):
	__tablename__ = 'authors'

	author_id = Column(Integer, primary_key=True)
	first_name = Column(String(length=50))
	last_name = Column(String(length=50))

	def __repr__(self):
		return "<Author(author_id='{0}', first_name='{1}', last_name='{2}'>".
			format(self.author_id, self.first_name, self.last_name)

class Book(Base):
	__tablename__ = 'books'

	book_id = Column(Integer, primary_key=True)
	title = Column(String(length=50))
	number_of_pages = Column(Integer)

	def __repr__(self):
		return "<Book(book_id='{0}', title='{1}', number_of_pages='{2}'>".
			format(self.book_id, self.title, self.number_of_pages)

class BookAuthor(Base):
	__tablename__ = 'bookauthors'

	bookauthor_id = Column(Integer, primary_key=True)
	author_id = Column(Integer, ForeignKey('authors.author_id'))
	book_id = Column(Integer, ForeignKey('books.book_id'))

	author = relationship("Author")
	book = relationship("Book")

	def __repr__(self):
		return '''<BookAuthor(bookauthor_id='{0}', 
			author_first_name='{1}', author_last_name='{2}',
			book_title='{3}'>'''.
			format(self.bookauthor_id, self.author.first_name, 
				self.author.last_name, self.book.title)

Base.metadata.create_engine(engine)

def create_session():
	session = sessionmaker(bind=engine)
	return session()

def add_book(title, number_of_pages, first_name, last_name):

if __name__ = "__main__":
	print("Input new book:\n")
	title = input("What is the title of the book?\n")
	number_of_pages = int(input("How many pages are in the book?\n"))
	first_name = input("What is the first name of the author?\n")
	last_name = input("What is the last name of the author?\n")
	print("Inputting book data:\n")

	add_book(title, number_of_pages, first_name, last_name)

	print("Done!")
