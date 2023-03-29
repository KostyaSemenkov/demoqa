from pages.text_box import TextBox
import time


def test_clear(browser):
    textbox = TextBox(browser)
    textbox.visit()
    textbox.first_pole.send_keys('dada')
    time.sleep(2)
    textbox.first_pole.clear()
    time.sleep(2)
    assert textbox.first_pole.get_text() == ''