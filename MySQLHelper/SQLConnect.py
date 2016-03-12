import MySQLdb

class SQLConnect: 
	def connect(self):
		self.db = MySQLdb.connect(host="localhost", user="john", passwd="megajonhy", db="jonhydb")
		self.cur = self.db.cursor(MySQLdb.cursors.DictCursor)
	
	def disconnect(self):
		self.db.close()

	def executeQuery(self, query):
		self.cur.execute(query)

	def fetchResults(self):
		for row in self.cur.fetchall:
			yield row


		 
