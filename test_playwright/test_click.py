#
# def test(driver):
#     driver.goto(
#         url="/buttons",
#         timeout=60000,
#         wait_until="load"
#     )
#
#     button_loc = "button[id='doubleClickBtn']"
#     text_loc = "p[id='doubleClickMessage']"
#
#     driver.locator(button_loc).dblclick()
#     text = driver.locator(text_loc).text_content()
#     assert text == "You have done a double click"
#

# def test(driver):
#     driver.goto(
#         url="/buttons",
#         wait_until="domcontentloaded"
#     )
#
#     button_loc = "button[id='doubleClickBtn']"
#     text_loc = "p[id='doubleClickMessage']"
#
#     driver.locator(button_loc).dblclick()
#     text = driver.locator(text_loc).text_content()
#     assert text == "You have done a double click"

# def test(driver):
#     driver.goto(
#         url="/buttons",
#         wait_until="commit"
#     )
#
#     button_loc = "button[id='doubleClickBtn']"
#     text_loc = "p[id='doubleClickMessage']"
#
#     driver.locator(button_loc).dblclick()
#     text = driver.locator(text_loc).text_content()
#     assert text == "You have done a double click"

def test(driver):
    driver.goto(
        url="/buttons",
        wait_until="domcontentloaded"
    )

    button_loc = "button[id='rightClickBtn']"
    text_loc = "p[id='rightClickMessage']"

    driver.locator(button_loc).click(button="right")
    text = driver.locator(text_loc).text_content()
    assert text == "You have done a right click"