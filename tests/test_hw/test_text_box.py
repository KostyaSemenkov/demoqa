from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    name = 'Kostya'
    text_box.first_pole.send_keys(name)
    address = 'My address'
    text_box.current_address.send_keys(address)
    text_box.btn_submit.click()
    transf='\n'
    bottom = (f'Name:Kostya{transf}Current Address :My address')
    assert text_box.bottom_pole.get_text() == bottom
