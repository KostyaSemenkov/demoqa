from pages.form_page import FormPage
import time


def test_send_keys(browser):

    send_key1 = FormPage(browser)
    send_key1.visit()
    send_key1.first_name.send_keys('Kostya')
    send_key1.last_name.send_keys('Semenkov')
    send_key1.telefon.send_keys('+79213718910')
    send_key1.sex.click()
    time.sleep(5)