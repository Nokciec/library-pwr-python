from firebase import firebase


class DatabaseConnection:
	firebase = firebase.FirebaseApplication('https://library-pwr.firebaseio.com', None)

	def get_data(query_string):
		return DatabaseConnection.firebase.get(query_string, None)

	def send_data(query_string, object_to_send):
		return DatabaseConnection.firebase.post(query_string, object_to_send.__dict__)

	def delete_data(url, name):
		DatabaseConnection.firebase.delete(url, name)