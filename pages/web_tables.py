from pages.base_page import BasePage
from components.components import WebElement


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.user_form = WebElement(driver, '#userForm')
        self.btn_close = WebElement(driver, 'div.modal-header > button > span.sr-only')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.user_email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')
        self.string4 = WebElement(driver, 'div.rt-tbody > div:nth-child(4)')
        self.pole_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(1)')
        self.reg_form = WebElement(driver, '//*[@class="fade modal show"]', 'xpath')
        self.pole_last_name = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(2)')
        self.pole_age = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(3)')
        self.pole_email = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(4)')
        self.pole_salary = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(5)')
        self.pole_department = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(6)')
        self.pensil = WebElement(driver, '#edit-record-4')
        self.basket = WebElement(driver, '#delete-record-4')
        self.select_5row = WebElement(driver, ' span.select-wrap.-pageSizeOptions > select > option:nth-child(1)')
        self.select_rows = WebElement(driver, 'span.select-wrap.-pageSizeOptions > select')
        self.btn_prev = WebElement(driver, 'div.-previous > button')
        self.btn_next = WebElement(driver, ' div.-next > button')
        self.num_page = WebElement(driver, 'span.-pageInfo > div > input[type=number]')
        self.num_of_pages = WebElement(driver, 'span.-pageInfo > span')
        self.btn_tables = WebElement(driver, 'div.rt-noData') # невидимый обьект, появляется когда нет строчек в таблице
        self.btn_basket = WebElement(driver, '[title="Delete"]') # неуникальный локатор корзины
        # div.rt - table > div.rt - thead. - header > div > div локатор столбика неуникальный
        # self.a =
        # self.b =
        # self.sc = WebElement(driver, f'div: nth - child({self.a}) > div > div:nth - child({self.b})')

