from BookList import BookList
from DatabaseConnection import DatabaseConnection as DC
import datetime
from flask import session

class Library(BookList):
	def __init__(self, path):
		self.path = path
		self.load_books()

	def add_book(self,book):
		book.save(self.path)
		
		self.load_books()

	def delete_book(self, book):
		DC.delete_data(self.path, book.book_ID)
		self.load_books()

	def rent_book(self,book_id,login):
		book_path = self.path +'/'+ book_id + '/'
		DC.firebase.put(book_path,'book_availability', False)
		DC.firebase.put(book_path, 'book_borrower_login',login)
		DC.firebase.put(book_path, 'book_reserver_login', '')
		DC.firebase.put(book_path, 'book_reservation', False)		

		start_date = datetime.datetime.now()
		end_date = start_date + datetime.timedelta(days=30)

		DC.firebase.put(book_path, 'book_startdate', start_date.strftime("%d/%m/%y"))
		DC.firebase.put(book_path, 'book_enddate', end_date.strftime("%d/%m/%y"))

		self.load_books()

	def return_book(self,book_id):
		book_path = self.path +'/'+ book_id + '/'
		DC.firebase.put(book_path,'book_availability', True)
		DC.firebase.put(book_path, 'book_borrower_login','')
		self.load_books()

	def reserve_book(self,book_id):
		book_path = self.path +'/'+ book_id + '/'
		DC.firebase.put(book_path,'book_reserver_login', session['username'])
		DC.firebase.put(book_path, 'book_reservation', True)
		self.load_books()

	def prolong(self,book_id):
		book_path = self.path +'/'+ book_id + '/'

		start_date = datetime.datetime.now()
		end_date = start_date + datetime.timedelta(days=30)

		DC.firebase.put(book_path, 'book_enddate', end_date.strftime("%d/%m/%y"))
		self.load_books()