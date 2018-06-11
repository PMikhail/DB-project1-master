import pandas as pd #show data as tables

# An implementation of the Individual class.
class ContactInfo:

	# Constructor
	def __init__(self, street, city, zip, state, phone=None, email=None):
		self._street = street
		self._city = city
		self._zip = zip
		self._state = state
		self._phone = phone
		self._email = email

	# Get the street
	#  @return street
	def getStreet(self):
		return self._street

	# Get the city
	#  @return id
	def getCity(self):
		return self._city

	def getZip(self):
		return self._zip

	def getState(self):
		return self._state
		
	def getPhone(self):
		return self._phone

	def getEmail(self):
		return self._email

	# Set the individual street.
	# @param street
	def setStreet(self, street):
		self._street = street

	# Set the individual street
	# @param id
	def setCity(self, city):
		self._city = city

	def setZip(self, zip):
		self._zip = zip

	def setState(self, state):
		self._state = state

	def setPhone(self, phone):
		self._phone = phone
	
	def setEmail(self, email):
		self.__email = email

	# Generate a string representation of the individual.
	# @return string representation
	def __str__(self):
		return str(self._street) +" "+ str(self._city) +" "+ str(self._zip) +" "+ str(self._state)

	@staticmethod
	def showAsTable(rows):
		df = pd.DataFrame(columns=["Street","City","Zip", "State", " Phone", "Email"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df
