from abc import ABC, abstractmethod
from DatabaseConnection import DatabaseConnection as DC
from Book import Book

class BookList(	):
	def __init__(self, path):
		self.path = path
		self.load_books()

	def load_books(self):
		self.books = []

		books_data = DC.get_data(self.path)

		for book_from_db_id in books_data:
			new_book = Book.empty()

			new_book.load(self.path + '/' + book_from_db_id)
			new_book.book_ID = book_from_db_id
			self.books.append(new_book)
