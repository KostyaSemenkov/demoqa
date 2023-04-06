from pages.accordion import Accordion
from pages.alerts import Alerts
from pages.demoqa import Demoqa
from pages.browser_tab import BrowserTab
import time
import pytest


@pytest.mark.parametrize('pages', [Demoqa, Alerts, BrowserTab, Accordion]) # посмотреть  элемент на нескольких страницах
def test_seo_meta(browser, pages):
    seo_meta = pages(browser)
    seo_meta.visit()
    time.sleep(2)
    assert seo_meta.meta_teg.exist()
    assert seo_meta.meta_teg.check_css('name') == 'viewport'
    assert seo_meta.meta_teg.check_css('content') =='width=device-width,initial-scale=1'

    
