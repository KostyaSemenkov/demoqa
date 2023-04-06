from pages.web_tables import WebTables


def test_sort_by(browser):
    sort_by = WebTables(browser)
    sort_by.visit()
    # num_pages = sort_by.num_of_pages.get_text()
    # for i in range(num_pages*10):
    #     while