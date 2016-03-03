from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FacebookObject:
	def __init__(self, webdriver, loginUsername, loginPassword):
		self.loginUsername = loginUsername
		self.loginPassword = loginPassword
		self.webdriver = webdriver

	def login(self):
		#Navigate to facebook 
		self.webdriver.get("https://www.facebook.com/")

		#enter the login information
		emailElem = self.webdriver.find_element_by_name("email")
		passElem = self.webdriver.find_element_by_name("pass")

		emailElem.send_keys(self.loginUsername)
		passElem.send_keys(self.loginPassword)

		passElem.send_keys(Keys.RETURN)
		
