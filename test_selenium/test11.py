
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
button = driver.find_element("css selector", "div[id='start']>button")

button.click()

text_field = driver.find_element("css selector", "div[id='finish']>h4")
print(text_field.text)

driver.quit()