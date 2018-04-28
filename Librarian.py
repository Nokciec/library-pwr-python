from  User import User
from DataModel import DataModel

class Librarian(User):

	def __init__(
		self,
		login,
		password,
		name,
		surname,
		):
		
		self.login = login
		self.password = password
		self.name = name
		self.surname = surname
		self.is_admin = True