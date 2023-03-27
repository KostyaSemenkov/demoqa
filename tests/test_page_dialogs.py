from pages.modal_dialogs import ModalDialogs
from pages.demoqa import Demoqa


def test_modal_elements(browser):
    test_modal = ModalDialogs(browser)
    test_modal.visit()
    assert test_modal.five_paragraph.check_count_elements(5)


def test_navigation_modal(browser):
    test_navigation = ModalDialogs(browser)
    test_navigation1 = Demoqa(browser)
    test_navigation.visit()
    test_navigation.refresh()
    test_navigation.icon.click()
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    assert test_navigation1.equal_url()
    assert test_navigation1.pageData['title'] == browser.title
    browser.set_window_size(1000, 1000)

