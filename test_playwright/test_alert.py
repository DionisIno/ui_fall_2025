"""
Alerts
https://demoqa.com/alerts
"""
import time


def test_confirm_alert_example(driver_demoqa):

    driver_demoqa.goto("alerts", wait_until="domcontentloaded")

    confirm_btn_loc = "button[id='confirmButton']"

    driver_demoqa.click(confirm_btn_loc)
    time.sleep(2)

def test_confirm_alert_accept(driver_demoqa):

    driver_demoqa.goto("alerts", wait_until="domcontentloaded")

    confirm_btn_loc = "button[id='confirmButton']"
    text_loc = "span[id='confirmResult']"

    driver_demoqa.once("dialog", lambda  dialog: dialog.accept())

    driver_demoqa.click(confirm_btn_loc)
    text = driver_demoqa.locator(text_loc).text_content()
    assert text == "You selected Ok"

def test_prompt_alert(driver_demoqa):

    driver_demoqa.goto("alerts", wait_until="domcontentloaded")

    confirm_btn_loc = "button[id='promtButton']"
    text_loc = "span[id='promptResult']"

    prompt_text = "Hello"

    driver_demoqa.once("dialog", lambda  dialog: dialog.accept(prompt_text))

    driver_demoqa.click(confirm_btn_loc)
    text = driver_demoqa.locator(text_loc).text_content()
    assert text == f"You entered {prompt_text}"