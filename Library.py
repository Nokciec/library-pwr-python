from BookList import BookList
from DatabaseConnection import DatabaseConnection as DC

class Library(BookList):
	def __init__(self, path):
		self.path = path
		self.load_books()

	def add_book(book):
		book.save(self.path)

	def delete_book(book):
		DC.delete_data(self.path, book.book_ID)