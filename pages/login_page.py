from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    # Locators
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")
    
    @allure.step("Open login page")
    def open(self):
        self.driver.get(self.URL)
    
    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    @allure.step("Get error message text")
    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
    
    @allure.step("Check if error message is displayed")
    def is_error_message_displayed(self):
        return self.is_element_visible(self.ERROR_MESSAGE)