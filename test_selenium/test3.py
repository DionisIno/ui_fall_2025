import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")
url = driver.current_url
title = driver.title
html = driver.page_source
time.sleep(2)
print()
print(url)
print(title)
print(html)
driver.quit()