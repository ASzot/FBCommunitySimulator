from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import mysql.connector

cnx = mysql.connector.connect(user = 'root', password = '?#s8EG!T,LRy', host='127.0.0.1', database='PersonData')



driver = webdriver.Firefox()
driver.get("https://accounts.google.com/SignUp?service=mail&continue=http%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-en")

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
verifyCapcha = driver.find_element_by_id("recaptcha_response_field")

firstNameElem.send_keys("Andrew")
lastNameElem.send_keys("Szot")
gmailAddElem.send_keys("andrew102992")

setPasswd = "onetwothree456"

passwdElem.send_keys(setPasswd)
confirmPasswdElem.send_keys(setPasswd)

selectBirthdayElem.click()
monthSelectOptionElem = driver.find_element_by_id(":a")
hover = ActionChains(driver).move_to_element(monthSelectOptionElem)
hover.send_keys(Keys.RETURN).perform()

birthDayElem.send_keys("25")
birthYearElem.send_keys("1997")

selectGenderElem.click()
genderSelectOptionElem = driver.find_element_by_id(":f")
hover = ActionChains(driver).move_to_element(genderSelectOptionElem)
hover.send_keys(Keys.RETURN).perform()

termsOfServiceElem.click()

verifyCapcha.send_keys("")


#driver.close()
