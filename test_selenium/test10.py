import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

file_path = r'E:\Program\PyCharm_program\red_rover\fall_2025\ui\download'
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

preferences = {
    "download.default_directory": file_path
}
options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://the-internet.herokuapp.com/download")
download_file = driver.find_element("css selector", "a[href*='TestFile.txt']")
download_file.click()
time.sleep(1)
driver.quit()