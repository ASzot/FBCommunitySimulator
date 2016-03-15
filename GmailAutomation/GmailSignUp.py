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
        if gender == "Female":
            genderSelection = ":e"
        elif gender == "Male":
            genderSelection = ":f"
        else:
            genderSelection = ":e"

        selectGenderElem.click()
        genderSelectOptionElem = driver.find_element_by_id(genderSelection)
        hover = ActionChains(driver).move_to_element(genderSelectOptionElem)
        hover.send_keys(Keys.RETURN).perform()

        # Check the terms of service check box.
        termsOfServiceElem.click()

        # Get the correct captcha from the user.
        captchaValue = str(raw_input("Please enter captcha..."))
        captchaElem.send_keys(captchaValue)

        submitBtn.click()

        if not self.__continueToGmail(driver):
            return self.__enterCellPhone(cellNumber, driver)

        self.__checkAdditionalLogin(driver)
        self.__closeGmailHelp(driver)

        return True


    def __checkAdditionalLogin(self, driver):
        try:
            passwdElem = driver.find_element_by_name("Passwd")
        except NoSuchElementException:
            return  # No Additional sign in required.

        # Additional sign in required.
        passwdElem.send_keys(self.setPasswd)

        signInBtnElem = driver.find_element_by_name("signIn")
        signInBtnElem.click()


    def __continueToGmail(self, driver):
        # It will either ask for a cell phone number to verify or it will create the email account.
        try:
            submitBtn = driver.find_element_by_name("submitbutton")
        except NoSuchElementException:
            # It is asking for a cell phone number.
            return False

        if submitBtn.get_attribute("value") != "Continue to Gmail":
            return False

        submitBtn.click()

        return True


    def __closeGmailHelp(self, driver):
        try:
            closeHelpBtn = driver.find_element_by_id("close-button")
            closeHelpBtn.click()
        except NoSuchElementException:
            pass  # There is no problem if there is no help screen just move on.



    def __enterCellPhone(self, cellNumber, driver):
        deviceNumElem = driver.find_element_by_name("deviceAddress")
        deviceNumElem.send_keys(cellNumber)

        continueBtn = driver.find_element_by_name("SendCode")
        continueBtn.click()

        verifEnterElem = driver.find_element_by_name("smsUserPin")
        continueBtn = driver.find_element_by_name("VerifyPhone")

        verifCode = str(raw_input("Enter verification code..."))

        verifEnterElem.send_keys(verifCode)
        continueBtn.click()

        if not self.__continueToGmail(driver):
            return False

        self.__checkAdditionalLogin(driver)
        self.__closeGmailHelp(driver)

        return True



