from pages.demoqa import Demoqa
from components.components import WebElement
from pages.elements_page import ElementsPage


def test_footer_check(browser):
    check_footer = Demoqa(browser)
    check_footer.visit()
    assert check_footer.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_text_centre(browser):
    check_text = Demoqa(browser)
    check_text.visit()
    check_text.btn_elements.click()
    check_text_elems = ElementsPage(browser)
    assert check_text_elems.text_please.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()

    # assert elements_page.text_elements.get_text() =='Elements'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()









