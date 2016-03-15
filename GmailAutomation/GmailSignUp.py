from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from random import randint


class GmailSignUp:
    def __init__(self):
        self.setPasswd = ""
        self.gmailAddress = ""


    def signUp(self, first, last, gender, birthDay, birthMonth, birthYear, driver, cellNumber):
        # Create random username
        randomFiveDigit = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        testUserName = first + last + randomFiveDigit
        # The maximum length for gmail is 30 characters.
        testUserName = testUserName[:30]

        driver.get("https://accounts.google.com/SignUp?service=mail&continue=http%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-en")

        # Get all of the elements of the web page.
        firstNameElem = driver.find_element_by_name("FirstName")
        lastNameElem = driver.find_element_by_name("LastName")
        gmailAddElem = driver.find_element_by_name("GmailAddress")
        passwdElem = driver.find_element_by_name("Passwd")
        confirmPasswdElem = driver.find_element_by_name("PasswdAgain")
        selectBirthdayElem = driver.find_element_by_id("BirthMonth")
        birthDayElem = driver.find_element_by_id("BirthDay")
        birthYearElem = driver.find_element_by_id("BirthYear")
        selectGenderElem = driver.find_element_by_id("Gender")
        termsOfServiceElem = driver.find_element_by_id("TermsOfService")
        captchaElem = driver.find_element_by_id("recaptcha_response_field")
        submitBtn = driver.find_element_by_name("submitbutton")

        submitBtn.click()

        firstNameElem.send_keys(first)
        lastNameElem.send_keys(last)
        gmailAddElem.send_keys(testUserName)

        self.gmailAddress = testUserName + "@gmail.com"

        self.setPasswd = "passwd"
        for i in range(0, 5):
            self.setPasswd += str(randint(0, 9))

        passwdElem.send_keys(self.setPasswd)
        confirmPasswdElem.send_keys(self.setPasswd)

        # Convert month to selection
        monthArray = [":1", ":2", ":3", ":4", ":5", ":6", ":7", ":8", ":9", ":a", ":b", ":c"]
        monthSelection = monthArray[birthMonth - 1]

        # Select the birth month in the dropdown menu
        selectBirthdayElem.click()
        monthSelectOptionElem = driver.find_element_by_id(monthSelection)
        hover = ActionChains(driver).move_to_element(monthSelectOptionElem)
        hover.send_keys(Keys.RETURN).perform()

        birthDayElem.send_keys(birthDay)
        birthYearElem.send_keys(birthYear)

        #convert gender to selection
        if gender == "female":
            genderSelection = ":e"
        if gender == "male":
            genderSelection = ":f"
        if gender == "other":
            genderSelection = ":g"

        selectGenderElem.click()
        genderSelectOptionElem = driver.find_element_by_id(genderSelection)
        hover = ActionChains(driver).move_to_element(genderSelectOptionElem)
        hover.send_keys(Keys.RETURN).perform()

        # Check the terms of service check box.
        termsOfServiceElem.click()

        # Get the correct captcha from the user.
        captchaValue = str(raw_input("Please enter captcha..."))
        captchaElem.send_keys(captchaValue)

        # It will either ask for a cell phone number to verify or it will create the email account.
        try:
            submitBtn = driver.find_element_by_name("submitbtn")
        except NoSuchElementException:
            # It is asking for a cell phone number.
            return self.__enterCellPhone(cellNumber, driver)

        if submitBtn.get_attribute("value") != "Continue to Gmail":
            return self.__enterCellPhone(cellNumber, driver)

        submitBtn.click()

        try:
            closeHelpBtn = driver.find_element_by_id("close-button")
            closeHelpBtn.click()
        except NoSuchElementException:
            pass  # There is no problem if there is no help screen just move on.

        return True

    def __enterCellPhone(self, cellNumber, driver):
        return False



