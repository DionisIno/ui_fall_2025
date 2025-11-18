import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# options.add_argument("--headless")
# options.add_argument("start-maximized")
# options.add_argument("--incognito")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1500,400")
# options.add_argument("--disable-cache")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.saucedemo.com/")
time.sleep(5)
driver.quit()