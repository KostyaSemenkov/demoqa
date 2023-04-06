from pages.demoqa import Demoqa
import pytest
from pages.alerts import Alerts
import time


def test_seo(browser):
    test_seo = Demoqa(browser)
    test_seo.visit()
    assert test_seo.pageData['title'] == browser.title


@pytest.mark.parametrize('pages', [Demoqa, Alerts])
def test_check_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert browser.title == page.pageData['title']



