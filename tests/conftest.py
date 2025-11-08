import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os


@pytest.fixture(scope="function")
def driver(request):
    """WebDriver fixture"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # TEMPORARILY DISABLE to debug
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver_path = ChromeDriverManager().install()
    if not driver_path.endswith('chromedriver.exe'):
        driver_dir = os.path.dirname(driver_path)
        potential_exe = os.path.join(driver_dir, 'chromedriver.exe')
        if os.path.exists(potential_exe):
            driver_path = potential_exe
        else:
            for root, dirs, files in os.walk(driver_dir):
                if 'chromedriver.exe' in files:
                    driver_path = os.path.join(root, 'chromedriver.exe')
                    break
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    yield driver
    
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG
        )
    
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


def pytest_configure(config):
    config.addinivalue_line("markers", "q1: Q1 tests")
    config.addinivalue_line("markers", "q2: Q2 tests")
    config.addinivalue_line("markers", "q3: Q3 tests")


def pytest_sessionfinish(session, exitstatus):
    allure_dir = session.config.getoption('--alluredir')
    if allure_dir and os.path.exists(allure_dir):
        env_properties = """Browser=Chrome
Platform=Windows
Python.Version=3.13.1
Test.Environment=QA
Application.URL=https://www.saucedemo.com
"""
        env_path = os.path.join(allure_dir, 'environment.properties')
        with open(env_path, 'w') as f:
            f.write(env_properties.strip())