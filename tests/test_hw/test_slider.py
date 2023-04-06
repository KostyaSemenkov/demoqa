from pages.slider import Slider
from selenium.webdriver import ActionChains


def test_slider(browser):
    slider_moving = Slider(browser)
    action_chains = ActionChains(browser)
    slider_moving.visit()
    assert slider_moving.btn_slider.exist()
    assert slider_moving.text_pole.exist()
    assert slider_moving.btn_slider.get_dom_attribute('value') == '25'
    action_chains.drag_and_drop_by_offset(slider_moving.btn_slider.find_element(), 1, 0 ).perform()
    assert slider_moving.text_pole.get_dom_attribute('value') == '50'
