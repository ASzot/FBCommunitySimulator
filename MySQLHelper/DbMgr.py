from MySQLHelper.SQLConnect import SQLConnect
from ProfileData import UserProfileData
from FacebookMining.FbDataMgr import FbDataMgr
import pickle

class DbMgr: 
	def __init__(self, sqlConnector):
		self.connector = sqlConnector


	def saveMinedLikeData(self):
		fbDataMgr = FbDataMgr.Instance()

		print "Saving all liked data!"
		print len(fbDataMgr.likeData)
		outputFile = open("../Data/all_like_data.txt", "w")
		pickle.dump(fbDataMgr.likeData, outputFile)


	def setupDatabase(self):
		self.connector.query("DROP TABLE IF EXISTS Persons")
		self.connector.query("CREATE TABLE Persons ("
							 "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
							 "gender VARCHAR(12),"
							 "interestedIn VARCHAR(12),"
							 "birthMonth TINYINT UNSIGNED,"
							 "birthDay TINYINT UNSIGNED,"
							 "birthYear SMALLINT UNSIGNED,"
							 "firstName VARCHAR(20),"
							 "lastName VARCHAR(20),"
							 "email VARCHAR(50),"
							 "emailPass VARCHAR(16),"
							 "facebookPass VARCHAR(16))")
		self.connector.query("DROP TABLE IF EXISTS Images")
		self.connector.query("CREATE TABLE Images ("
							 "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, "
							 "location VARCHAR(30),"
							 "userId INT(6) UNSIGNED)")

		self.connector.query("DROP TABLE IF EXISTS LikedPage")
		self.connector.query("CREATE TABLE LikedPage ("
							 "id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,"
							 "url VARCHAR(300) NOT NULL,"
							 "userId INT(6) UNSIGNED,"
							 "date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")


	def saveUserProfile(self, userProfile):
		self.connector.query("INSERT INTO Persons "
							 "(gender, interestedIn, birthMonth, birthDay, birthYear, firstName, lastName) "
							 "VALUES ('{}', '{}', {}, {}, {}, '{}', '{}')".format(userProfile.gender, userProfile.interestedIn, userProfile.birthMonth, userProfile.birthDay, userProfile.birthYear, userProfile.first, userProfile.last))

		# Save the user photo locations.
		lastInsertId = self.connector.getLastInsertId()
		for location in userProfile.userImages:
			self.connector.query("INSERT INTO Images (location, userId) VALUES ('{}', {})".format(location, lastInsertId))


	def saveUserProfileEmailData(self, userProfile):
		self.connector.query("UPDATE Persons SET email = '{}', emailPass = '{}' WHERE userId = {}".format(userProfile.emailAddress, userProfile.emailPasswd, userProfile.userId))

	def loadAllUserProfiles(self):
		self.connector.query("SELECT * FROM Persons")
		allUserProfiles = []
		results = self.connector.fetchResults()
		for result in results:
			userId = result["id"]

			# Get all of the images associated with the ID.
			self.connector.query("SELECT * FROM Images WHERE userId = {}".format(userId))
			imageResults = self.connector.fetchResults()
			imageLocations = []
			for imageResult in imageResults:
				imageLocations.append(imageResult["location"])

			userProfile = UserProfileData(result["gender"], result["interestedIn"], imageLocations)
										  
			userProfile.first = result["firstName"]
			userProfile.last = result["lastName"]
			userProfile.birthDay = result["birthDay"]
			userProfile.birthMonth = result["birthMonth"]
			userProfile.brithYear = result["birthYear"]

			userProfile.userId = result["id"]

			allUserProfiles.append(userProfile)

		return allUserProfiles


	def loadMinedLikedData(self):
		inputFile = open("../Data/all_like_data.txt", "r+")
		return pickle.load(inputFile)
