from pages.demoqa import Demoqa


def test_seo(browser):
    test_seo = Demoqa(browser)
    test_seo.visit()
    assert browser.title == 'DEMOQA'