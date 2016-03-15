from FacebookMining.FacebookObject import FacebookObject
from FacebookMining.ProfileMiner import ProfileMiner
from selenium import webdriver
from MySQLHelper.SQLConnect import SQLConnect
from MySQLHelper.DbMgr import DbMgr
from Core.NameFactory import NameFactory
from ProfileMgr import ProfileMgr
import time
import pickle


def collectUserInfo(dbMgr, driver, cred):
	fbObj = FacebookObject(driver, cred[0], cred[1])
	fbObj.login()

	time.sleep(3)
	outputFile = open("friends_output.txt", "r+")
	userFriends = pickle.load(outputFile)
	profileMiner = ProfileMiner(driver)

	nameFactory = NameFactory()

	for userFriend in userFriends:
		profileMiner.mineProfile(userFriend)
		profileObj = profileMiner.getProfileObj()

		if profileObj is not None:
			print "Saving user info"
			profileObj.genUserInfo(nameFactory)
			dbMgr.saveUserProfile(profileObj)

	dbMgr.saveMinedLikeData()


def createAccounts(dbMgr, profileMgr):
	profileMgr.users = dbMgr.loadAllUserProfiles()
	# Update all the user's in the database with their email address and password.
	profileMgr.createAccountGmails(dbMgr)


def run(dbMgr):
	pass

with open("cred.txt") as credFile:
	cred = [line.rstrip('\n') for line in credFile]

sqlConnect = SQLConnect(cred[2], cred[3], cred[4], cred[5])
sqlConnect.connect()

dbMgr = DbMgr(sqlConnect)



#ONLY RUN THIS THE FIRST TIME THE APPLICATION IS RUNNING
#dbMgr.setupDatabase()

driver = webdriver.Firefox()

# Either mine the data and save it to the database.
# This is creating the database and setting up the necessary data.
#collectUserInfo(dbMgr, driver, cred)

# Initial setup of all of the accounts.
profileMgr = ProfileMgr(driver, cred[6])
createAccounts(dbMgr, profileMgr)

# Or use the data already present in the database to load and update the users 
#run(dbMgr)

sqlConnect.disconnect()

time.sleep(3)
driver.close()
