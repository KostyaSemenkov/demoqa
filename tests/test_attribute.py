from pages.text_box import TextBox


def test_attribute_holder(browser):
    holder = TextBox(browser)
    holder.visit()
    assert holder.first_pole.get_dom_attribute('placeholder') == 'Full Name'