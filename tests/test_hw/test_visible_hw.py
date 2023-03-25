from pages.accordion import Accordion
from pages.elements_page import WebElement
import time


def test_visible_accordion(browser):
    content_accordion = Accordion(browser)
    content_accordion.visit()
    assert content_accordion.content.visible()
    content_accordion.header.click()
    time.sleep(2)
    assert not content_accordion.content.visible()

def test_visible_accordion_default(browser):
    accordion_default = Accordion(browser)
    accordion_default.visit()
    assert not accordion_default.content2.visible()
    assert not accordion_default.content3.visible()
    assert not accordion_default.content4.visible()



