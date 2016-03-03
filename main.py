from FacebookMining.FacebookObject import FacebookObject
from FacebookMining.ProfileMiner import ProfileMiner
from selenium import webdriver
import time
import pickle

driver = webdriver.Firefox()

#Enter your own username and password here."
fbObj = FacebookObject(driver, "USERNAME", "PASSWORD")

fbObj.login()

time.sleep(3)

outputFile = open("friends_output.txt", "r+")
userFriends = pickle.load(outputFile)

profileMiner = ProfileMiner(driver)
profileMiner.mineProfile(userFriends[0])


time.sleep(3)

driver.close()
