import urllib
import time
from selenium.common.exceptions import NoSuchElementException 
from Core.FuncHelper import *
from FacebookData.FbDataMgr import FbDataMgr
from ProfileData import ProfileData


class ProfileMiner:
	MAX_PHOTOS_PER_USER = 10
	def __init__(self, driver):
		self.driver = driver
		self.likesData = []
	@staticmethod
	def getUserFriends(driver, profileURL):
		# Return the list of all of a user's friends in an array.
		driver.get(profileURL + "/friends")
		
		continueSearching = True
		while continueSearching:
			continueSearching = False
			try:
				driver.find_element_by_id("medley_header_photos")
			except NoSuchElementException:
				continueSearching = True

			driver.execute_script("document.getElementById('pageFooter').scrollIntoView(false)")
			time.sleep(2)

		allFriendsData = []
		allFriends = driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']");
		for friendLinkContainer in allFriends:

			friendLink = friendLinkContainer.find_element_by_tag_name("a")
			friendLinkDest = friendLink.get_attribute("href")
			friendLinkDest = friendLinkDest.split("&")[0]
			print friendLinkDest
			allFriendsData.append(friendLinkDest)

		return allFriendsData


	def getProfileObj(self):
		profileObj = UserProfileData(self.likeData, self.genderData, self.interestedIn)	
		return profileObj


	def mineProfile(self, profileURL):
		self.profileURL = profileURL.split("?")[0]

		self.__minePics()
		self.__mineLikes()
		self.__mineInfo()


	def __getDataFor(self, dataFieldLblName):
		
		dataLblElem = self.driver.find_element_by_xpath("//*[contains(text(), '{0}')]".format(dataFieldLblName))
		dataRowElem = dataLblElem.find_element_by_xpath("../..")
		dataRowContainer = dataRowElem.find_element_by_xpath("//div[@class='_4bl7 _pt5']").find_element_by_class_name('_50f4')
		return dataRowContainer.text


	def __mineInfo(self): 
		self.driver.get(self.profileURL + "/about?section=contact-info&pnref=about")

		try: 
			self.genderData = self.__getDataFor("Gender");
		except NoSuchElementException:
			self.genderData = None

		try:
			self.interestedIn = self.__getDataFor("Interested In")
		except NoSuchElementException:
			self.interestedIn = None


	def __mineLikes(self):
		self.driver.get(self.profileURL + "/likes")
		
		fbDataMgr = FbDataMgr.getInstance()

		# TOOD Make a way to get all of the user's likes. 
		#self.driver.execute_script("$(#pageFooter).scrollIntoView()")

		allLikedPages = self.driver.find_elements_by_xpath("//div[@class='fsl fwb fcb']");

		for likedPage in allLikedPages:
			# Get the link child
			likedPageLink = likedPage.find_element_by_tag_name("a")

			# Get the link location 
			likedPageDest = likedPageLink.get_attribute("href")
			fbDataMgr.addLikeData(likedPageDest)
		


	def __minePics(self):
		self.driver.get(self.profileURL + "/photos")

		profilePicElem = self.driver.find_element_by_class_name("profilePic")
		profileImgSrc = profilePicElem.get_attribute("src")

		uniqueSaveName = get_a_uuid()

		urllib.urlretrieve(profileImgSrc, "images/" + uniqueSaveName + ".png")

		# Next save all of the images that the user has in their albums. 
		albumEles = self.driver.find_elements_by_xpath("//a[contains(@class,'uiMediaThumb')]")
		
		linkDests = []
		for albumEle in albumEles:
			linkDest = albumEle.get_attribute("href")
			linkDests.append(linkDest)

		imgSrcDests = []
		for linkDest in linkDests:
			self.driver.get(linkDest)

			shouldContinue = True
			while shouldContinue:
				nextBtnElem = self.driver.find_element_by_xpath("//a[contains(@class, 'next')]")
				nextBtnElem.click()
				time.sleep(1)

				photoElem = self.driver.find_element_by_class_name("spotlight")
				imgSrc = photoElem.get_attribute("src")

				if (imgSrc in imgSrcDests):
					shouldContinue = False
				else:
					imgSrcDests.append(imgSrc)

				if len(imgSrcDests) > self.MAX_PHOTOS_PER_USER:
					shouldContinue = False
			if len(imgSrcDests) > self.MAX_PHOTOS_PER_USER:
				break

		for imgSrcDest in imgSrcDests:
			self.driver.get(imgSrcDest)
			# Save the image. 
			uniqueSaveName = get_a_uuid()
			urllib.urlretrieve(imgSrcDest, "images/" + uniqueSaveName + ".png")



