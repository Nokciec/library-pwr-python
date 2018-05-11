from DataModel import DataModel

class User(DataModel):
	
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
		self.is_admin = is_admin
		

	@classmethod
	def empty(cls):
		"""
		Empty constructor, use only when the object is about to get loaded from database
		"""
		return cls(None, None, None, None, None)
