from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'

        super().__init__(driver, self.base_url)
        self.pageData={
        'title': 'DEMOQA'

        }
        self.five_paragraph = WebElement(driver, 'div:nth-child(1) > div > div > div:nth-child(3) > div > ul >li')
        self.icon = WebElement(driver, '#app > header >a')
        self.small_modal = WebElement(driver, '#showSmallModal')
        self.large_modal = WebElement(driver, '#showLargeModal')
        self.modal_dialog_window = WebElement(driver, 'div.fade.modal.show')
        self.small_close = WebElement(driver, '#closeSmallModal')
        self.large_close = WebElement(driver, '#closeLargeModal')
        self.not_have = WebElement(driver, '#main-message > h1 > span')