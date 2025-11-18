import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

time.sleep(10)

driver.quit()