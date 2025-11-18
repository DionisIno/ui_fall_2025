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

driver.get("https://demoqa.com/alerts")
# alert_button = driver.find_element("css selector", "button[id='timerAlertButton']")
# alert_button = driver.find_element("css selector", "button[id='confirmButton']")
alert_button = driver.find_element("css selector", "button[id='promtButton']")

wait.until(EC.element_to_be_clickable(alert_button)).click()

alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
alert.send_keys("QWERTY")

time.sleep(5)
alert.accept()
# alert.dismiss()
time.sleep(5)

driver.quit()