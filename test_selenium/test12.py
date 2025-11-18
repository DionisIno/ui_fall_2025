
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 2, poll_frequency=1)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
button = driver.find_element("css selector", "div[id='start']>button")

button.click()

text_field = ("css selector", "div[id='finish']>h4")
# text = wait.until(EC.visibility_of_element_located(text_field)).text
text = wait.until(EC.visibility_of_element_located(text_field), message="Мы не дождались появления текста").text
print(text)

driver.quit()