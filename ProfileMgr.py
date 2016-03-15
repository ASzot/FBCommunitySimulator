from ProfileData import UserProfileData
from GmailAutomation.GmailSignUp import GmailSignUp

class ProfileMgr:

	def __init__(self, driver, cellNum):
		self.users = []
		self.driver = driver
		self.cellNum = cellNum

	def createAccountGmails(self, dbMgr):
		gmailSignuper = GmailSignUp()

		for user in self.users:
			if not gmailSignuper.signUp(user.first, user.last, user.gender, user.birthDay, user.birthMonth, user.birthYear, self.driver, self.cellNum):
				raise Exception("Gmail sign up failed.")

			# Save the user's generated data.
			user.emailAddress = gmailSignuper.gmailAddress
			user.emailPasswd = gmailSignuper.setPasswd

			dbMgr.saveUserProfileEmailData(user)
