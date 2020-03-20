from selenium import webdriver
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckOutPage
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")

class TestEnd2End(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        time.sleep(5)
        #home_page.shop_items().click()
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # check_out_page = CheckOutPage(self.driver)
        check_out_page = home_page.shop_items()
        cards = check_out_page.get_card_title()
        log.info("getting all the card titles.")
        i = -1
        for card in cards:
            i = i + 1
            card_text = card.text
            log.info(card_text)
            if card_text == "Blackberry":
                check_out_page.get_card_footer()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        confirm_page = check_out_page.get_check_out_items()

        self.driver.find_element_by_id("country").send_keys("ind")
        log.info("Entered country name as ind")
        '''
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(By.LINK_TEXT, "India"))
        '''
        self.is_link_presence("India")
        time.sleep(3)

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_xpath("//input[@value='Purchase']").click()
        text_match = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is" + text_match)

        assert ("Success! Fail for test Thank you!" in text_match)




