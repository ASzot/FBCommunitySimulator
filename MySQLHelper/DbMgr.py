from FacebookData.ProfileMiner import DbMgr.py
from MySQLHelper.SQLConnect import SQLConnect

class DbMgr: 
	def __init__(self, sqlConnector):
		self.connector = sqlConnector

	def saveUserProfile(self, userProfile):
		#TODO:
		# Put the code for saving a user's profile here.

	def loadAllUserProfiles(self):
		#TODO:
		# Load all of the user profiles and return them in an arrray

	def saveMinedLikeData(self, profileMiner):
		#TODO:
		# Save all of the likes from the profile miner here. 

	def loadMinedLikedData(self):
		#TODO:
		# Load of all the data from the database it should be an array of the URL pages of the pages that could be liked
