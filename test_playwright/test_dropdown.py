"""
Dropdown
https://the-internet.herokuapp.com/dropdown
"""
import time

dropdown_loc = "select[id='dropdown']"

def test_dropdown_value(driver_herokuapp):

    driver_herokuapp.goto("/dropdown")

    driver_herokuapp.select_option(dropdown_loc, value="1")

    assert driver_herokuapp.locator(dropdown_loc).input_value() == "1"

def test_dropdown_index(driver_herokuapp):

    driver_herokuapp.goto("/dropdown")

    driver_herokuapp.select_option(dropdown_loc, index=2)

    assert driver_herokuapp.locator(dropdown_loc).input_value() == "2"

def test_dropdown_label(driver_herokuapp):

    driver_herokuapp.goto("/dropdown")

    driver_herokuapp.select_option(dropdown_loc, label="Option 2")

    selected_option = driver_herokuapp.locator(f"{dropdown_loc} option:checked").inner_text()

    assert selected_option == "Option 2"
