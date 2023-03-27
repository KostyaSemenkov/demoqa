from pages.elements_page import ElementsPage


def test_find_elements(browser):
    test_find = ElementsPage(browser)
    test_find.visit()
    assert test_find.btn_first_menu.check_count_elements(9)