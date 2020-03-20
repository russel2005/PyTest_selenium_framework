import pytest
from selenium import webdriver as wd

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = wd.Chrome(executable_path="C:\\Drivers\\chromedriver.exe")
        print("Chrome driver started")
    elif browser_name == "firefox":
        driver = wd.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
        print("Firefox driver started")
    elif browser_name == "opera":
        driver = wd.Edge(executable_path="c:\\Drivers\\operadriver.exe")
        print("Opera driver started")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):

    #timestamp = datetime.now().strftime('%H-%M-%S')

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        """
        feature_request = item.funcargs['request']
        driver = feature_request.getfixturevalue('browser')
        driver.save_screenshot('D:/report/scr' + timestamp + '.png')

        extra.append(pytest_html.extras.image('D:/report/scr' + timestamp + '.png'))

        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        """
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;"' \
                       'onclick="window.open(this.src)" align="right" /></div>' %file_name
            #extra.append(pytest_html.extras.image('D:/report/scr.png'))
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

