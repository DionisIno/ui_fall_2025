import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")

# name = driver.find_element(By.CSS_SELECTOR, "input[data-test='username']")
# password = driver.find_element(By.CSS_SELECTOR, "input[data-test='password']")
# button = driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']")

name = driver.find_element("css selector", "input[data-test='username']")
password = driver.find_element("css selector", "input[data-test='password']")
button = driver.find_element("css selector", "input[data-test='login-button']")

name.send_keys("standard_user")
time.sleep(2)
password.send_keys("secret_sauce")
time.sleep(2)
button.click()
time.sleep(5)
