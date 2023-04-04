from pages.alerts import Alerts
import time
import allure


@allure.title("Проверка алерта")
def test_alerts(browser):
    test_alert = Alerts(browser)
    test_alert.visit()
    assert not test_alert.alert()
    test_alert.btn_alert.click()
    time.sleep(2)
    assert test_alert.alert()
    test_alert.alert().accept()

@allure.title('Подтверждение алерта')
def test_alert_text(browser):
    alert_text = Alerts(browser)
    alert_text.visit()
    alert_text.btn_alert.click()
    time.sleep(2)
    assert alert_text.alert().text == 'You clicked a button'
    alert_text.alert().accept()
    assert not alert_text.alert()

@allure.title('Отмена алерта')
def test_confirm(browser):
    confirm = Alerts(browser)
    confirm.visit()
    confirm.confirm_btn.click()
    time.sleep(2)
    confirm.alert().dismiss()
    assert confirm.block.get_text() == 'You selected Cancel'


@allure.title('Ввод имени')
def test_prompt(browser):
    promt_send = Alerts(browser)
    promt_send.visit()
    promt_send.promt.click()
    time.sleep(2)
    promt_send.alert().send_keys('Kostik')
    promt_send.alert().accept()
    assert promt_send.name.get_text() == 'You entered Kostik'




