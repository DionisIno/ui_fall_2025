import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
driver = webdriver.Chrome(service=service, options=options)


driver.get("https://demoqa.com/upload-download")

upload_file = driver.find_element("css selector", "input[id='uploadFile']")
file_path = r"E:\Program\PyCharm_program\red_rover\fall_2025\ui\sampleFile.jpeg"
upload_file.send_keys(file_path)
time.sleep(5)
driver.quit()