from pages.text_box import TextBox
import allure


def test_attribute_holder(browser):
    holder = TextBox(browser)
    holder.visit()
    assert holder.first_pole.get_dom_attribute('placeholder') == 'Full Name'


@allure.feature('check attr')# название блока тестов
@allure.story('Проверка отсутствия атрибута') # описание самого теста
@allure.severity(allure.severity_level.BLOCKER) # серьезность бага
def test_placeholder(browser):
    pass