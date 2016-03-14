import MySQLdb

class SQLConnect: 
	def __init__(self, host, user, passwd, db):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.db = db
	
	def connect(self):
		self.db = MySQLdb.connect(host=self.host, user=self.user, passwd=self.passwd, db=self.db)
		self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)
	
	def disconnect(self):
		self.db.close()

	def query(self, query):
		self.cur.execute(query)

	def fetchResults(self):
		for row in self.cur.fetchall:
			yield row


		 
