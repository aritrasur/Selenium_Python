from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()
browser.get ('http://www2.ea.com/sports')

wait=WebDriverWait(browser,5)

browser.save_screenshot('/Users/aritrasur/desktop/screenprint.png')
browser.quit()
