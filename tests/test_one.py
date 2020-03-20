from selenium import webdriver as wd

def test_open_browser():

    #driver = wd.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
    driver = wd.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
    driver.get("https://www.google.com")