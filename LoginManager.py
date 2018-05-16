import CONSTANTS
from DatabaseConnection import DatabaseConnection as DC
from User import User

class LoginManager:
	@staticmethod
	def authenticate(login, password):

		users_data = DC.get_data(CONSTANTS.USERS_TABLE)

		for user_id in users_data:

			user = User.empty()

			user.load(CONSTANTS.USERS_TABLE + '/' + user_id)
			
			if user.login == login:
				if user.password == password:
					if user.is_admin:
						return CONSTANTS.LOGIN_ADMIN
					else:
						return CONSTANTS.LOGIN_CLIENT

				else:
					return CONSTANTS.LOGIN_FAILED

		return CONSTANTS.LOGIN_FAILED
