import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.saucedemo.com/")

print()
name = driver.find_element("css selector", "input[data-test='username']")
password = driver.find_element("css selector", "input[data-test='password']")
button = driver.find_element("css selector", "input[data-test='login-button']")

name_before = name.get_attribute("value")
name.send_keys("standard_user")
time.sleep(1)
name_after = name.get_attribute("value")

# a = name.get_attribute("class")
# b = name.get_attribute("type")
# c = name.get_attribute("placeholder")
#
#
# print(name_before)
# print(name_after)
# print(a)
# print(b)
# print(c)

a1 = button.value_of_css_property("background-color")
print(a1)
driver.quit()