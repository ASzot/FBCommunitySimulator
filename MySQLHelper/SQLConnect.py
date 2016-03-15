import MySQLdb

class SQLConnect: 
	def __init__(self, host, user, passwd, db):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.dbName = db
	
	def connect(self):
		print "Connecting to " + self.host + " as " + self.user + " with the password " + self.passwd + " on " + self.dbName

		self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.dbName)
		self.cur = self.db.cursor()


	def disconnect(self):
		self.db.close()


	def getLastInsertId(self):
		return self.cur.lastrowid


	def query(self, query):
		try:
			self.cur.execute(query)
			self.db.commit()
		except:
			self.db.rollback()


	def fetchResults(self):
		for row in self.cur.fetchall:
			yield row


		 
