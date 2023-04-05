from pages.modal_dialogs import ModalDialogs

# Нет подключения к Интернету
def test_small_large_modal(browser):
    modal_dial_btns = ModalDialogs(browser)
    modal_dial_btns.visit()
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

