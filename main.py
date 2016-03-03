from FacebookMining.FacebookObject import FacebookObject
from FacebookMining.ProfileMiner import ProfileMiner
from selenium import webdriver
import time
import pickle

driver = webdriver.Firefox()

fbObj = FacebookObject(driver, "farfanfefe@gmail.com", "utug5,p23x")

fbObj.login()

time.sleep(3)

outputFile = open("friends_output.txt", "r+")
userFriends = pickle.load(outputFile)

profileMiner = ProfileMiner(driver)
profileMiner.mineProfile(userFriends[0])


time.sleep(3)

driver.close()
