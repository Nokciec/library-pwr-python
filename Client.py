from  User import User

class Client(User):

	def __init__(
		self,
		login,
		password,
		name,
		surname,
		is_admin
		):
		
		self.login = login
		self.password = password
		self.name = name
		self.surname = surname
		self.is_admin = False