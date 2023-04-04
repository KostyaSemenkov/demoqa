import time
import allure
from pages.web_tables import WebTables


@allure.feature('DEMOQA')
@allure.story('Проверка формы ввода данных')
@allure.severity(allure.severity_level.CRITICAL)
def test_filling_data(browser):
    filling_data = WebTables(browser)
    filling_data.visit()
    filling_data.btn_add.click()
    time.sleep(1)
    filling_data.btn_submit.click()
    assert filling_data.user_form.get_dom_attribute('class') == 'was-validated'
    browser.refresh()
    time.sleep(1)
    filling_data.btn_add.click()
    filling_data.first_name.send_keys('tester')
    filling_data.last_name.send_keys('testerov')
    filling_data.user_email.send_keys('test@test.tst')
    filling_data.age.send_keys('36')
    filling_data.salary.send_keys('1000')
    filling_data.department.send_keys('QA')
    filling_data.btn_submit.click()
    time.sleep(1)
    assert filling_data.btn_add.visible()
    assert filling_data.pole_name.get_text() == 'tester'
    assert filling_data.pole_last_name.get_text() == 'testerov'
    assert filling_data.pole_email.get_text() == 'test@test.tst'
    assert filling_data.pole_age.get_text() == '36'
    assert filling_data.pole_salary.get_text() == '1000'
    assert filling_data.pole_department.get_text() == 'QA'
    filling_data.pensil.click()
    assert filling_data.btn_add.visible()
    filling_data.first_name.clear()
    filling_data.first_name.send_keys('t')
    filling_data.btn_submit.click()
    time.sleep(1)
    assert filling_data.pole_name.get_text() == 't'
    filling_data.basket.click()
    assert filling_data.pole_name.get_text() == ' '
    assert filling_data.pole_last_name.get_text() == ' '
    assert filling_data.pole_email.get_text() == ' '
    assert filling_data.pole_age.get_text() == ' '
    assert filling_data.pole_salary.get_text() == ' '
    assert filling_data.pole_department.get_text() == ' '


@allure.feature('DEMOQA')
@allure.story('Проверка использования кнопок Next и Preview')
@allure.severity(allure.severity_level.NORMAL)
def test_arrows_next_prev(browser):
    next_prev_arrows = WebTables(browser)
    next_prev_arrows.visit()
    next_prev_arrows.select_rows.scroll_to_element()
    next_prev_arrows.select_rows.click()
    next_prev_arrows.select_5row.click()
    assert next_prev_arrows.btn_prev.get_dom_attribute('disabled class') == False
    assert next_prev_arrows.btn_next.get_dom_attribute('disabled class') == False
    next_prev_arrows.btn_add.click()
    next_prev_arrows.first_name.send_keys('tester')
    next_prev_arrows.last_name.send_keys('testerov')
    next_prev_arrows.user_email.send_keys('test@test.tst')
    next_prev_arrows.age.send_keys('36')
    next_prev_arrows.salary.send_keys('1000')
    next_prev_arrows.department.send_keys('QA')
    next_prev_arrows.btn_submit.click()
    time.sleep(1)
    next_prev_arrows.btn_add.click()
    next_prev_arrows.first_name.send_keys('tester1')
    next_prev_arrows.last_name.send_keys('testerov1')
    next_prev_arrows.user_email.send_keys('test1@test.tst')
    next_prev_arrows.age.send_keys('36')
    next_prev_arrows.salary.send_keys('1000')
    next_prev_arrows.department.send_keys('QA')
    next_prev_arrows.btn_submit.click()
    time.sleep(1)
    next_prev_arrows.btn_add.click()
    next_prev_arrows.first_name.send_keys('tester2')
    next_prev_arrows.last_name.send_keys('testerov2')
    next_prev_arrows.user_email.send_keys('test2@test.tst')
    next_prev_arrows.age.send_keys('36')
    next_prev_arrows.salary.send_keys('1000')
    next_prev_arrows.department.send_keys('QA')
    next_prev_arrows.btn_submit.click()
    time.sleep(1)
    assert next_prev_arrows.num_of_pages.get_text() == '2'
    assert next_prev_arrows.btn_next.get_dom_attribute('class') == '-btn'
    next_prev_arrows.btn_next.click()
    assert next_prev_arrows.num_page.get_dom_attribute('value') == '2'
    next_prev_arrows.btn_prev.click()
    assert next_prev_arrows.num_page.get_dom_attribute('value') == '1'


@allure.title('Проверка блока No rows found')
def test_no_row_found(browser):
    no_row = WebTables(browser)
    no_row.visit()
    assert not no_row.btn_tables.exist()
    while no_row.btn_basket.exist() == True:
        no_row.btn_basket.click()
    time.sleep(2)
    assert no_row.btn_tables.get_text() == 'No rows found'




