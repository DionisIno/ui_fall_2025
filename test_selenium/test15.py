import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"


driver = webdriver.Chrome(service=service, options=options)

wait = WebDriverWait(driver, 10, poll_frequency=1)
action = ActionChains(driver)


driver.get("https://demoqa.com/buttons")
double_button = ("css selector", "button[id='doubleClickBtn']")
button = wait.until(EC.visibility_of_element_located(double_button))
time.sleep(1)
action.double_click(button).perform()
time.sleep(15)
driver.quit()