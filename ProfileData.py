from random import randint

class UserProfileData:

    def __init__(self, gender, interestedIn, userImages):
        self.emailAddress = ""
        self.emailPasswd = ""
        self.userId = -1
        self.gender = gender
        if self.gender == "None":
            self.gender = "Male"

        self.interestedIn = interestedIn
        if self.interestedIn == "None":
            if self.gender == "Male":
                self.interestedIn = "Female"
            elif self.gender == "Female":
                self.interestedIn = "Male"
            else:
                self.interestedIn = "Female"

        self.userImages = userImages


    def genUserInfo(self, nameFactory):
        if self.gender == "Male":
            self.first = nameFactory.getFemaleFirstName()
        else:
            self.first = nameFactory.getFemaleFirstName()

        self.last = nameFactory.getLastName()

        # Just to be sure that this is a valid day in all months.
        self.birthDay = randint(0, 28)
        self.birthMonth = randint(0, 12)

        # From 1987 to 1999.
        self.birthYear = randint(1987, 1999)

