from DataModel import DataModel


class Book(DataModel):

	@classmethod
	def empty(cls):
		"""
		Empty constructor, use only when the object is about to get loaded from database
		"""
		return cls(None, None, None, None, None, None, None, None, None, None, None, None, None, None)

	def __init__(
		self,
		book_ID,
		book_title,
		book_author,
		book_ISBN,
		book_publicationDate,
		book_publicationPlace,
		book_publisher,
		book_pagesNumber,
		book_availability,
		book_borrower_login,
		book_startdate,
		book_enddate,
		book_reservation,
		book_reserve_login):

		self.book_ID = book_ID
		self.book_title = book_title
		self.book_author = book_author;
		self.book_ISBN = book_ISBN
		self.book_publisher = book_publisher
		self.book_publicationPlace = book_publicationPlace
		self.book_publicationDate = book_publicationDate
		self.book_pagesNumber = book_pagesNumber
		self.book_availability = book_availability
		self.book_borrower_login = book_borrower_login
		self.book_startdate = book_startdate
		self.book_enddate = book_enddate
		self.book_reservation = book_reservation
		self.book_reserve_login = book_reserve_login


	@staticmethod
	def create_new_library_book(
		book_title,
		book_author,
		book_ISBN,
		book_publicationDate,
		book_publicationPlace,
		book_publisher,
		book_pagesNumber
		):

		return Book(
		0, #TODO: CHECK
		book_title,
		book_author,
		book_ISBN,
		book_publicationDate,
		book_publicationPlace,
		book_publisher,
		book_pagesNumber,
		True, 
		'',
		'',
		'',
		False,
		''
		)
