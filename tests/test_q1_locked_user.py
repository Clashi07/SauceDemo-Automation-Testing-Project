
import pytest
import allure
from pages.login_page import LoginPage
@pytest.mark.q1
def test_locked_out_user_error_message(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    
    assert login_page.is_error_message_displayed()
    error_message = login_page.get_error_message()
    expected = "Epic sadface: Sorry, this user has been locked out."
    assert error_message == expected