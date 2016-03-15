from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from random import randint


class GmailSignUp:
    def __init__(self):
        pass

    def signUp(self, first, last, gender, birthDay, birthMonth, birthYear, driver):
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

        firstNameElem.send_keys(first)
        lastNameElem.send_keys(last)
        gmailAddElem.send_keys(testUserName)

        # For now just make the password static for all of the users
        setPasswd = "passwd19291"

        passwdElem.send_keys(setPasswd)
        confirmPasswdElem.send_keys(setPasswd)

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
