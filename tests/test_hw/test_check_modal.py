from pages.modal_dialogs import ModalDialogs
import pytest
@pytest.mark.xfail(condition=True, reason="Если страница недоступна, то тест будет пропущен")
def test_small_large_modal(browser):
    modal_dial_btns = ModalDialogs(browser)
    modal_dial_btns.visit()
    assert modal_dial_btns.icon.exist()
    assert modal_dial_btns.small_modal.exist()
    assert modal_dial_btns.large_modal.exist()
    modal_dial_btns.small_modal.click()
    assert modal_dial_btns.modal_dialog_window.exist()
    modal_dial_btns.small_close.click()
    assert not modal_dial_btns.modal_dialog_window.exist()
    modal_dial_btns.large_modal.click()
    assert modal_dial_btns.modal_dialog_window.exist()
    modal_dial_btns.large_close.click()
    assert not modal_dial_btns.modal_dialog_window.exist()

