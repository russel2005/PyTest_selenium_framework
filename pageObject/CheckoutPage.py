from selenium.webdriver.common.by import By
from pageObject.ConfirmPage import ConfirmPage

class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    card_title = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    check_out = (By.XPATH, "//button[@class='btn btn-success']")

    def get_card_title(self):
        return self.driver.find_elements(*CheckOutPage.card_title)

    def get_card_footer(self):
        return self.driver.find_elements(*CheckOutPage.card_footer)

    def get_check_out_items(self):
        self.driver.find_elements(*CheckOutPage.check_out)
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
