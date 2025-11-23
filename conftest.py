import pytest
from playwright.sync_api import Playwright, ViewportSize


@pytest.fixture
def driver(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

# @pytest.fixture
# def driver(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False, slow_mo=1000)
#     context = browser.new_context()
#     page = context.new_page()
#     page.set_default_timeout(10000)
#     yield page
#     page.close()
#     context.close()
#     browser.close()

@pytest.fixture
def driver_herokuapp(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1440, height=980),
        base_url="https://the-internet.herokuapp.com"
    )
    page = context.new_page()
    page.set_default_timeout(10000)
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture
def driver_demoqa(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(
        viewport=ViewportSize(width=1600, height=1000),
        base_url="https://demoqa.com/"
    )
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()