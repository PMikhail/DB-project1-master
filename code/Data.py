import psycopg2

from DBUtils import DBUtils
from Individual import Individual
from SocWork import SocWork

# @param boundle address
# @return a dictionary containing the connection information

def getBundle(filepath, sep='=', comment_char='#'):
	props = {}
	with open(filepath, "rt") as f:
		for line in f:
			l = line.strip()
			if l and not l.startswith(comment_char):
				key_value = l.split(sep)
				key = key_value[0].strip()
				value = sep.join(key_value[1:]).strip().strip('"')
				props[key] = value
	return props

# An implementation of the Data
class Data:

	def __init__(self):
		self._conn = None
		self._bundle = None

# Open a database connection.
#
# @param boundle address
# @return connection
	def  openDBConnectionWithBundle(self, bundle):
		prop =getBundle(bundle)
		return self.openDBConnection(prop['dbUser'],prop['dbPass'],prop['dbSID'],prop['dbHost'],prop['dbPort'])

# Open the database connection.
# @param dbUser
# @param dbPass
# @param dbSID
# @param dbHost
# @return
	def openDBConnection(self, dbUser,dbPass,dbSID,dbHost,port):
		if (self._conn != None):
			self.closeDBConnection()
		try:
			self._conn = DBUtils.openDBConnection(dbUser, dbPass, dbSID, dbHost, port)
			res = DBUtils.testConnection(self._conn)
		except psycopg2.Error as e:
			print (e)
		return res

# Close the database connection.
	def closeConnection(self):
		try:
			DBUtils.closeConnection(self._conn)
		except psycopg2.Error as e:
			print (e)

# Get all participants, their issues and socia workers.
# @return
	def getIndividuals(self):
		query = ("select i.ssn, i.name, iss.name, s.name, s.title, i.date_joined, ci.street || ' ' || ci.city || ' ' || ci.state || ', ' || ci.zip as Address "
	"from individuals i, social_workers s, issues iss, contact_info ci "
					"where i.social_worker=s.ssn and i.issue=iss.iid and i.contact_info = ci.cid")
		return DBUtils.getAllRows(self._conn,query)

	def getWorkers_And_Clients(self, orderByClause):
		query = ("select w.name as \"Social Worker\", w.title as Title, count(i.ssn) as \"Num of clients\", min(i.sw_since) as \"Oldest Current Client\" "
					"from social_workers w left join individuals i on w.ssn=i.social_worker "
					"group by w.name, w.specialization, w.title "
					"order by %s" % orderByClause)
		return DBUtils.getAllRows(self._conn, query)

	def getIssues(self):
		query = "select iss.name, iss.iid from issues iss "
		rows = DBUtils.getAllRows(self._conn,query)
		issues = []
		for val in rows:
			issues.append(val[0])
		return issues

	def getWorkers(self):
		query = "select w.name, w.ssn from social_workers w "
		rows = DBUtils.getAllRows(self._conn,query)
		workers = []
		for val in rows:
			workers.append(val[0])
		return workers

	def registerIndividual(self, newContactInfo, newClient):
		try :
			query = """
					insert into Contact_Info (street, city, zip, state) values (%s,%s,%s,%s)
				"""
			DBUtils.executeUpdate(self._conn, query,(newContactInfo.getStreet(), newContactInfo.getCity(), newContactInfo.getZip(), newContactInfo.getState()))
			cid = DBUtils.getVar(self._conn, "select max(cid) from Contact_Info")
			i_issue = DBUtils.getVar(self._conn, "select iid from Issues where name='%s'" % newClient.getIssue())
			worker_ssn = DBUtils.getVar(self._conn, "select ssn from Social_Workers where name='%s'" % newClient.getWorker())
			query = """
					insert into Individuals (ssn, name, date_joined, issue, social_worker, sw_since, contact_info) values (%s,%s,%s,%s,%s,%s,%s)
				"""
			DBUtils.executeUpdate(self._conn, query,(newClient.getSSN().strip(), newClient.getName(), newClient.getDateJoined().strftime('%m-%d-%Y'), i_issue, worker_ssn.strip(), newClient.getWorkerSince().strftime('%m-%d-%Y'), cid));
		except psycopg2.Error as e:
			print (e)
		return newClient
    
	def search(self, name):
		query = """
        select s.ssn, s.name, 'Social Worker' as type, ci.State 
        from social_workers s, contact_info ci
        where lower(s.name) like '%%%s%%' and s.contact_info=ci.cid
        UNION 
        select i.ssn, i.name, 'Individual' as type, ci.State
        from Individuals i, contact_info ci 
        where lower(i.name) like '%%%s%%' and i.contact_info=ci.cid 
        order by 1""" % (name.lower(), name.lower())
		return DBUtils.getAllRows(self._conn, query)
    
	def display_worker_no_clients(self):
		query = """
        SELECT w.ssn, w.name, w.title, iss.name as Specialization, ci.state as "State Of Operation"
        FROM   social_workers w, issues iss, contact_info ci
        WHERE  w.ssn NOT IN (SELECT i.social_worker
                       FROM   individuals i, 
                              social_workers w
                       WHERE  w.ssn = i.social_worker) 
        and w.specialization=iss.iid and w.contact_info = ci.cid"""
		return DBUtils.getAllRows(self._conn, query)
    
	def display_statistics(self):
		query = """
        select iss.name, c.state, count(iss.iid)
        from individuals i, issues iss, contact_info c
        where i.issue=iss.iid and i.contact_info=c.cid
        group by iss.name, c.state
        order by iss.name, count(iss.iid) desc, c.state"""
		return DBUtils.getAllRows(self._conn, query)
    