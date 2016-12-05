import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#open gmail
browser= webdriver.Chrome()
browser.get("https://mail.google.com")

#Enter email id
emailid= browser.find_element_by_id('Email')
emailid.send_keys('nova.cloc@gmail.com')

#Click on Next button
nextButton= browser.find_element_by_id('next')
nextButton.click()

#Enter Password
password = WebDriverWait(browser, 10).until(
   EC.presence_of_element_located((By.ID, 'Passwd')))
password.send_keys('ondway#1')

#Click on SignIn
signInButton = browser.find_element_by_id('signIn')
signInButton.click()

#Compose Email
Composeemail= WebDriverWait(browser,10).until(
		EC.presence_of_element_located((By.XPATH, "//div[text()='COMPOSE']")))
Composeemail.click()

#Input to
mailto = browser.find_element_by_name("to")
mailto.send_keys('aritra@flywheel.com')

#Mail Subject
entersubject= WebDriverWait(browser,10)
entersubject= browser.find_element_by_name("subjectbox")
entersubject.send_keys('Auto mail test with Selenium')

#Mail Body
mailBody = browser.find_element_by_css_selector("div[aria-label='Message Body']")
mailBody.send_keys('This is an auto generated email. Please Ignore.')
time.sleep(5)

#Hit Send
sendmail = WebDriverWait(browser,10)
sendmail = browser.find_element_by_xpath("//div[text()='Send']")
sendmail.click()

#logout Gmail
logout1 = WebDriverWait(browser,10)
logout1 = browser.find_element_by_class_name('gbii')
logout1.click()

logout2 = browser.find_element_by_id("gb_71")
logout2.click()

time.sleep(3)
browser.quit()
