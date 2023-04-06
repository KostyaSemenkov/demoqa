from pages.droppable import Droppable
import time
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    drag_drop = Droppable(browser)
    drag_drop.visit()
    action_chains = ActionChains(browser)
    # assert not drag_drop.drop.check_css('backgroundColor')
    action_chains.drag_and_drop(drag_drop.drag.find_element(), drag_drop.drop.find_element()).perform()
    time.sleep(1)
    # assert drag_drop.drop.check_css('backgroundColor') == 'steelblue'
    action_chains.drag_and_drop_by_offset(drag_drop.drag.find_element(), -200, 0 ).perform()
    time.sleep(2)
    # assert drag_drop.drop.check_css('backgroundColor') == 'steelblue'
