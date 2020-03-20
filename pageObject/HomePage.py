from selenium.webdriver.common.by import By
from pageObject.CheckoutPage import CheckOutPage

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")
    success_msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def shop_items(self):
        # return self.driver.find_element(*HomePage.shop)
        # * = particular variable as tuple
        # driver.find_element_by_css_selector("a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)

    def get_alert_text(self):
        return self.driver.find_element(*HomePage.success_msg)
