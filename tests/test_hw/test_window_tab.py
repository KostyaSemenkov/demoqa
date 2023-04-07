from pages.links import Links


def test_window_tab(browser):
    window_tab = Links(browser)
    window_tab.visit()
    assert window_tab.btn_home.get_text() == 'Home'
    assert window_tab.btn_home.get_dom_attribute('href') == 'https://demoqa.com'
    num_tab = len(browser.window_handles)
    window_tab.btn_home.click()
    assert len(browser.window_handles) == num_tab + 1
