"""
Drag and drop
https://demoqa.com/droppable
"""



def test_simple_drag_and_drop(driver_demoqa):

    driver_demoqa.goto("dragabble", wait_until="domcontentloaded")

    drag_loc = "div[id='dragBox']"

    drag = driver_demoqa.locator(drag_loc)

    before = drag.bounding_box()

    x_coord = before["x"] + 300
    y_coord = before["y"] + 300

    driver_demoqa.locator(drag_loc).hover()
    driver_demoqa.mouse.down()

    driver_demoqa.mouse.move(x_coord, y_coord)
    driver_demoqa.mouse.up()

    after = drag.bounding_box()

    assert before["x"] != after["x"] and before["y"] != after["y"]

