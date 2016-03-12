from FacebookMining.FacebookObject import FacebookObject
from FacebookMining.ProfileMiner import ProfileMiner
from selenium import webdriver
from MySQLHelper.SQLConnect import SQLConnect
from MySQLHelper.DbMgr import DbMgr
from Core.NameFactory import NameFactory
import time
import pickle


def collectUserInfo(dbMgr, driver):
	#Enter your own username and password here."
	fbObj = FacebookObject(driver, "USERNAME", "PASSWORD")

	fbObj.login()

	outputFile = open("friends_output.txt", "r+")
	userFriends = pickle.load(outputFile)
	profileMiner = ProfileMiner(driver)

	nameFactory = NameFactory()

	for userFriend in userFriends:
		profileMiner.mineProfile(userFriend)
		profileObj = profileMiner.getProfileObj()
		profileObj.genUserInfo(nameFactory)
		dbMgr.saveUserProfile(profileObj)

	dbMgr.saveMinedLikedData(profileMiner)


def run(dbMgr):
	pass

sqlConnect = SQLConnect()
sqlConnect.connect()

dbMgr = DbMgr(sqlConnect)

driver = webdriver.Firefox()

# Either mine the data and save it to the database.
# This is creating the database and setting up the necessary data.
collectUserInfo(dbMgr, driver)

# Or use the data already present in the database to load and update the users 
#run(dbMgr)

sqlConnect.disconnect()

time.sleep(3)
driver.close()
