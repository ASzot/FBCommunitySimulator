from FacebookMining.FacebookObject import FacebookObject
from FacebookMining.ProfileMiner import ProfileMiner
from selenium import webdriver
from MySQLHelper.SQLConnect import SQLConnect
from MySQLHelper.DbMgr import DbMgr
import time
import pickle


def collectUserInfo(dbMgr):
	outputFile = open("friends_output.txt", "r+")
	userFriends = pickle.load(outputFile)
	profileMiner = ProfileMiner(driver)

	for userFriend in userFriends:
		profileMiner.mineProfile(userFriends[0])
		dbMgr.saveUserProfile(profileMiner.getUserProfile
	# To avoid making too many calls to facebook too fast and seeming like a robot. 
	time.sleep(3)

def run(dbMgr):
	
	


sqlConnect = SQLConnect() 
dbMgr = DbMgr(sqlConnect)

driver = webdriver.Firefox()

#Enter your own username and password here."
fbObj = FacebookObject(driver, "USERNAME", "PASSWORD")

fbObj.login()

# Either mine the data and save it to the database.
# This is creating the database and setting up the necessary data.
#collectUserInfo(dbMgr)

# Or use the data already present in the database to load and update the users 
#run(dbMgr)

time.sleep(3)
driver.close()
