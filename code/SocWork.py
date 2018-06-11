import pandas as pd #show data as tables

# An implementation of the Individual class.
class SocWork:

	# Constructor
	def __init__(self, name, ssn, title, date_started):
		self._name = name
		self._ssn = ssn
		self._title = title
		self._joindate = date_started

	# Getter
	def getName(self):
		return self._name

	# Get the ssn
	#  @return id
	def getSSN(self):
		return self._ssn

	def getTitle(self):
		return self._title

	def getJoinDate(self):
		return self._joindate

	# Setter
	def setName(self, name):
		self._name = name

	def setSSN(self, ssn):
		self._ssn = ssn
	
	def setTitle(self, title):
		self._title = title

	def setJoinDate(self, date_started):
		self._joindate = date_started

	# Generate a string representation of the social workers.
	# @return string representation
	def __str__(self):
		return str(self._ssn) +" "+ str(self._name) +" "+ str(self._title) +" "+ str(self._joindate)

	# Show a list of students as panda table.
	# @return panda dataframe
	@staticmethod
	def showAsTable(rows):
		df = pd.DataFrame(columns=["SSN","Social Worker Name","Title", "Date Joined"])
		for i in rows:
			df.loc[df.shape[0]] = i
			return df
	
	@staticmethod
	def showAsWACTable(rows):
		df = pd.DataFrame(columns=["Social Worker", "Title", "Num of Clients", "Oldest Current Client"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df
	@staticmethod
	def showWorkersNoClientsAsTable(rows):
		df = pd.DataFrame(columns=["SSN", "Name", "Title", "Specialization", "State Of Operation"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df
