from abc import ABC, abstractmethod
from DatabaseConnection import DatabaseConnection as DC

class DataModel(ABC):
	def save(self, path):
		DC.send_data(path, self)

	def load(self, path):
		self.__dict__ = DC.get_data(path)