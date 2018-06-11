import pandas as pd #show data as tables

# An implementation of the Individual class.
class Individual:

	# Constructor
	def __init__(self, ssn, name, dateJoined=None, issue=None, worker=None, worker_since=None):
		self._name = name
		self._ssn = ssn
		self._dateJoined = dateJoined
		self._issue = issue
		self._worker = worker
		self._worker_since = worker_since

	# Get the name
	#  @return name
	def getName(self):
		return self._name

	# Get the ssn
	#  @return id
	def getSSN(self):
		return self._ssn

	def getDateJoined(self):
		return self._dateJoined

	def getIssue(self):
		return self._issue
		
	def getWorker(self):
		return self._worker

	def getWorkerSince(self):
		return self._worker_since

	# Set the individual name.
	# @param name
	def setName(self, name):
		self._name = name

	# Set the individual name
	# @param id
	def setSSN(self, ssn):
		self._ssn = ssn

	def setDateJoined(self, dateJoined):
		self._dateJoined = dateJoined

	def setIssue(self, issue):
		self._issue = issue

	def setWorker(self, worker):
		self._worker = worker
	
	def setWorkerSince(self, worker_since):
		self._worker_since = worker_since

	# Generate a string representation of the individual.
	# @return string representation
	def __str__(self):
		return str(self._ssn) +" "+ str(self._name) +" "+ str(self._issue) +" "+ str(self._worker)

	# Show a list of students as panda table.
	# @return panda dataframe
	@staticmethod
	def showAsTable(rows):
		df = pd.DataFrame(columns=["SSN","Individual Name","Issue", "Social Worker", " Social Worker's Title", "Date Joined", "Address"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df
    
    
    
	# Show a list of everyone for a search resul
    
	# @return panda dataframe
	@staticmethod
	def showSearchResults(rows):
		df = pd.DataFrame(columns=["SSN", "Name","Client/Soc Worker", "State"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df

    	# @return panda dataframe
	@staticmethod
	def showStatistics(rows):
		df = pd.DataFrame(columns=["Issue", "State","# of cases"])
		for i in rows:
			df.loc[df.shape[0]] = i
		return df