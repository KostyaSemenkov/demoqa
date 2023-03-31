from pages.text_box import TextBox
import allure


def test_attribute_holder(browser):
    holder = TextBox(browser)
    holder.visit()
    assert holder.first_pole.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('check attr')
def test_placeholder(browser):
    pass