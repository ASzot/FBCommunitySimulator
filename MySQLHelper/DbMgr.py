from MySQLHelper.SQLConnect import SQLConnect
from ProfileData import UserProfileData
import pickle

class DbMgr: 
	def __init__(self, sqlConnector):
		self.connector = sqlConnector

	# WARNING ALL DATA WILL BE DELETED
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
							 "(gender, interestedIn, birthMonth, birthDay, birthYear, firstName, lastName "
							 "VALUES ({}, {}, {}, {}, {}, {}, {})".format(userProfile.gender,
																		  userProfile.interestedIn,
																		  userProfile.birthMonth,
																		  userProfile.birthDay,
																		  userProfile.birthYear,
																		  userProfile.firstName,
																		  userProfile.lastName))


	def loadAllUserProfiles(self):
		self.connector.query("SELECT * FROM Persons")
		allUserProfiles = []
		for result in self.connector.fetchResults():
			userProfile = UserProfileData(result["gender"],
										  result["interestedIn"],
										  result["firstName"],
										  result["lastName"],
										  result["birthDay"],
										  result["birthMonth"],
										  result["birthYear"])
			allUserProfiles.append(userProfile)

		return allUserProfiles


	def saveMinedLikeData(self, profileMiner):
		outputFile = open("Data/all_like_data.txt", "w")
		pickle.dump(profileMiner.likesData, outputFile)


	def loadMinedLikedData(self):
		inputFile = open("Data/all_like_data.txt", "r+")
		return pickle.load(inputFile)
