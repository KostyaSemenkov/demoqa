import time

from pages.form_page import FormPage


def test_login_form_validate(browser):
    test_login_form = FormPage(browser)
    test_login_form.visit()
    assert test_login_form.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert test_login_form.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert test_login_form.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert test_login_form.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$'
    test_login_form.btn_submit.click_force()
    assert test_login_form.user_form.get_dom_attribute('class') == 'was-validated'


def test_pole_state_city(browser):
    pole_state = FormPage(browser)
    pole_state.visit()

    pole_state.btn_state.send_keys('NCR')
    pole_state.btn_state.btn_enter()
    time.sleep(2)

    pole_state.btn_city.send_keys('Delhi')
    pole_state.btn_city.btn_enter()
    pole_state.btn_submit.click_force()
    time.sleep(2)


