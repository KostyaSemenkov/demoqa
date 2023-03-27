from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage

def test_navigator(browser):

    elements_pages = ElementsPage(browser)
    test_navigator = Demoqa(browser)
    test_navigator.visit()
    test_navigator.btn_elements.click()
    test_navigator.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert elements_pages.equal_url()