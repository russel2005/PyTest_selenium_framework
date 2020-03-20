import pytest

from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_form_submission(self):

        home_page = HomePage(self.driver)
        home_page.get_name().send_keys("Russel")
        home_page.get_email().send_keys("russel@gmail.com")
        home_page.get_checkbox().click()
        #sel = Select(home_page.get_gender())
        #sel.select_by_visible_text("Male")
        self.select_option_by_text(home_page.get_gender(), "Male")
        home_page.submit_form().click()
        success_msg = home_page.get_alert_text().text

        assert ("Success" in success_msg)

    @pytest.mark.skip
    def test_form_submission_with_data_driven(self, get_data):

        home_page = HomePage(self.driver)
        home_page.get_name().clear()
        home_page.get_name().send_keys(get_data[0])
        home_page.get_email().clear()
        home_page.get_email().send_keys(get_data[1])
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), get_data[2])
        home_page.submit_form().click()
        success_msg = home_page.get_alert_text().text

        assert ("Success" in success_msg)

    @pytest.fixture(params=[("russel", "russel@gmail.com", "Male"), ("arish", "arish@gmail.com", "Male")])
    def get_data(self, request):
        return request.param


    def test_form_submission_with_dict_data_driven(self, get_dict_data):

        home_page = HomePage(self.driver)
        home_page.get_name().clear()
        home_page.get_name().send_keys(get_dict_data["fname"])
        home_page.get_email().clear()
        home_page.get_email().send_keys(get_dict_data["email"])
        home_page.get_checkbox().click()
        self.select_option_by_text(home_page.get_gender(), get_dict_data["gender"])
        home_page.submit_form().click()
        success_msg = home_page.get_alert_text().text

        assert ("Success" in success_msg)

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    #@pytest.fixture(params=[{"fname": "russel", "email": "russel@gmail.com", "gender": "Male"}, {"fname": "arish", "email": "arish@gmail.com", "gender": "Male"}])
    def get_dict_data(self, request):
        return request.param
