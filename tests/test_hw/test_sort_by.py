from pages.web_tables import WebTables


def test_sort_by(browser):
    sort_by = WebTables(browser)
    sort_by.visit()
    assert sort_by.column_first_name.get_dom_attribute('class') == sort_by.column_last_name.get_dom_attribute('class') == sort_by.column_age.get_dom_attribute('class') == sort_by.column_email.get_dom_attribute('class') == sort_by.column_salary.get_dom_attribute('class') == sort_by.column_department.get_dom_attribute('class') =='rt-th rt-resizable-header -cursor-pointer'
    sort_by.column_first_name.click()
    assert sort_by.column_first_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort_by.column_last_name.click()
    assert sort_by.column_last_name.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort_by.column_age.click()
    assert sort_by.column_age.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort_by.column_salary.click()
    assert sort_by.column_salary.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort_by.column_email.click()
    assert sort_by.column_email.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    sort_by.column_department.click()
    assert sort_by.column_department.get_dom_attribute('class') == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'

