from pages.text_box import TextBox


def test_text_box_submit(browser):
    box_sub = TextBox(browser)
    box_sub.visit()
    assert box_sub.btn_submit.check_css('color', '#fff')
    assert box_sub.btn_submit.check_css('backgroundColor', '#fff')
    assert box_sub.btn_submit.check_css('borderColor', '#fff')
