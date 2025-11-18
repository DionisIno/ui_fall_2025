import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

# options.page_load_strategy = "normal"
# options.page_load_strategy = "eager"
# options.page_load_strategy = "none"

driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://www.saucedemo.com/")

start_time = time.time()
driver.get("https://demoqa.com/")
end_time = time.time()
print(end_time - start_time)
driver.quit()