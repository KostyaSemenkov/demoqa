from pages.form_page import FormPage
import time


def test_send_keys(browser):

    send_key1 = FormPage(browser)
    send_key1.visit()
    assert not send_key1.modal_dialog.exist()
    time.sleep(2)
    send_key1.first_name.send_keys('tester')
    send_key1.last_name.send_keys('testerovich')
    send_key1.user_number.send_keys('9992223344')
    send_key1.gender_radio_1.click_force()
    time.sleep(2)
    send_key1.user_email.send_keys('test@ttt.tt')
    time.sleep(2)
    send_key1.btn_submit.click_force()
    time.sleep(2)
    assert send_key1.modal_dialog.exist()
    send_key1.btn_close_modal.click_force()

