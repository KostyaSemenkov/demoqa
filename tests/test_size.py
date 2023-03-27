from pages.demoqa import Demoqa
import time


def test_size(browser):
    test_size = Demoqa(browser)
    test_size.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
