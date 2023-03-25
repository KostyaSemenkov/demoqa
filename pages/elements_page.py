from pages.base_page import BasePage
# from selenium.common.exceptions import NoSuchElementException
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):

        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.text_please = WebElement(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, '#app > div > div > div.pattern-backgound.playgound-header > div')
        self.btn_sidebar_first = WebElement(driver, '#app > div > div > div.row > div:nth-child(1) > div > div > div:nth-child(1) > span > div > div.header-text')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.icon = WebElement(driver, '#app > header >a')
        self.btn_sidebar_first_checkbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        # self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

    # def exist_icon(self):
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

