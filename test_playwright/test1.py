import time

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")
    time.sleep(1)
    page.locator("[data-test=\"username\"]").fill("standard_user")
    time.sleep(1)
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    time.sleep(1)
    page.locator("[data-test=\"login-button\"]").click()
    time.sleep(5)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)