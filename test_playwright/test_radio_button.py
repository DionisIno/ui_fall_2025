

def test_radio_button_yes(driver_demoqa):
    driver_demoqa.goto(
        url="radio-button",
        wait_until="domcontentloaded"
    )

    yes_radio_btn_loc = "label[for='yesRadio']"
    yes_text_loc = "span[class='text-success']"

    driver_demoqa.locator(yes_radio_btn_loc).check()

    text = driver_demoqa.locator(yes_text_loc).text_content()

    assert text == "Yes"

def test_radio_button_impressive(driver_demoqa):
    driver_demoqa.goto(
        url="radio-button",
        wait_until="domcontentloaded"
    )

    yes_radio_btn_loc = "label[for='impressiveRadio']"
    impressive_text_loc = "span[class='text-success']"

    driver_demoqa.locator(yes_radio_btn_loc).check()

    text = driver_demoqa.locator(impressive_text_loc).text_content()

    assert text == "Impressive"