from random import choice


class NameFactory:
    def __init__(self):
        with open("Data/male_names.txt", "r+") as maleInput:
            self.maleNames = []
            for maleInputLine in maleInput:
                afterNameIndex = maleInputLine.find(" ")
                self.maleNames.append(maleInputLine[:afterNameIndex])

        with open("Data/female_names.txt", "r+") as femaleInput:
            self.femaleNames = []
            for femaleInputLine in femaleInput:
                afterNameIndex = femaleInputLine.find(" ")
                self.femaleNames.append(femaleInputLine[:afterNameIndex])

        with open("Data/last_names.txt", "r+") as lastInput:
            self.lastNames = []
            for lastInputLine in lastInput:
                afterNameIndex = lastInputLine.find(" ")
                self.lastNames.append(lastInputLine[:afterNameIndex])

    def getFemaleFirstName(self):
        return choice(self.femaleNames)

    def getMaleFirstName(self):
        return choice(self.maleNames)

    def getLastName(self):
        return choice(self.lastNames)

