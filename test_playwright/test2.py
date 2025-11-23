
from playwright.sync_api import expect


# def test(driver):
#     driver.goto("https://www.saucedemo.com/")

#     username_loc = "//input[@data-test='username']"
#     password_loc = "input[data-test='password']"
#     button_loc = "//input[@data-test='login-button']"
#
#     driver.locator(username_loc).fill("standard_user")
#     driver.locator(password_loc).fill("secret_sauce")
#     driver.locator(button_loc).click()
#     url = driver.url
#     title = driver.title()

#     assert title == "Swag Labs" and url == "https://www.saucedemo.com/inventory.html", "Some error text"

# def test(driver):
#     driver.goto("https://www.saucedemo.com/")

#     username_loc = "//input[@data-test='username']"
#     password_loc = "input[data-test='password']"
#     button_loc = "input"
#     button_text = "Login"
#     text_loc = "//div[@class='app_logo']"
#
#     driver.locator(username_loc).fill("standard_user")
#     driver.locator(password_loc).fill("secret_sauce")
#     driver.locator(f'{button_loc}:has-text("{button_text}")').click()
#     expect(driver.locator(text_loc), "Text is not Swag Labs").to_have_text("Swag Labs")

# def test(driver):
#     driver.goto("https://www.saucedemo.com/")
#     username_loc = "//input[@data-test='username']"
#     password_loc = "input[data-test='password']"
#     button_loc = "//input[@data-test='login-button']"
#     error_text_loc = "h3[data-test='error']"
#     error_text = "Epic sadface: Sorry, this user has been locked out."
#     assert_error = f"Error text is not {error_text}"
#
#     driver.locator(username_loc).fill("locked_out_user")
#     driver.locator(password_loc).fill("secret_sauce")
#     driver.locator(button_loc).click()
#     expect(driver.locator(error_text_loc), assert_error).to_have_text(error_text)
