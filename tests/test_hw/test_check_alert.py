from pages.alerts import Alerts
import time


def test_check_timer(browser):
    check_timer = Alerts(browser)
    check_timer.visit()
    assert check_timer.timer_alert.exist()
    check_timer.timer_alert.click()
    assert not check_timer.alert()
    time.sleep(4)
    assert not check_timer.alert()
    time.sleep(1)
    assert check_timer.alert()
    check_timer.alert().accept()