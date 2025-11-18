import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.page_load_strategy = "eager"
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://demoqa.com/frames")

frame_window = ("css selector", "iframe[id='frame1']")

frame_text = ("css selector", "h1[id='sampleHeading']")

frame_window = wait.until(EC.visibility_of_element_located(frame_window))
driver.switch_to.frame(frame_window)

text = wait.until(EC.visibility_of_element_located(frame_text)).text

time.sleep(5)
print(text)

driver.quit()