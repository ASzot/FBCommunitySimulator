from random import randint

class UserProfileData:

    def __init__(self, gender, interestedIn, userImages):
        self.gender = gender
        self.interestedIn = interestedIn
        self.userImages = userImages

    def __init__(self, gender, interestedIn, first, last, birthDay, birthMonth, birthYear):
        self.gender = gender
        self.interestedIn = interestedIn
        self.first = first
        self.last = last
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear

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
