import pytest
import allure
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

@pytest.mark.q2
@allure.feature('Purchase Journey')
@allure.story('Standard User Complete Purchase')
@allure.title('Standard user purchase journey with cart and checkout verification')
def test_standard_user_purchase_journey(driver):
    # Initialize page objects
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # 1. Login
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    time.sleep(2)  # Wait for login
    
    # 2. From hamburger menu, reset the App State
    inventory_page.open_menu()
    time.sleep(1)
    inventory_page.reset_app_state()
    time.sleep(1)
    inventory_page.close_menu()
    time.sleep(1)
    
    # 3. Add any three items to the cart
    products = ["Sauce Labs Backpack", "Sauce Labs Bike Light", 
                "Sauce Labs Bolt T-Shirt"]
    for product in products:
        inventory_page.add_product_to_cart_by_name(product)
        time.sleep(0.5)  # Wait between additions
    
    # 4. Navigate to cart page (verify we're on the CART page, not checkout)
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    
    # Verify we're actually on cart page
    assert "cart.html" in driver.current_url, f"Expected cart page but got {driver.current_url}"
    
    # 5. Proceed to checkout
    cart_page.proceed_to_checkout()
    time.sleep(2)
    
    # 6. Fill checkout information and continue to final page
    checkout_page.fill_checkout_information("John", "Doe", "12345")
    checkout_page.click_continue()
    time.sleep(2)
    
    # 7. Verify product names on final checkout page
    displayed_products = checkout_page.get_all_product_names()
    for product in products:
        assert product in displayed_products, f"{product} not found in checkout"
    
    # 8. Verify total price
    total_price = checkout_page.get_total_price()
    assert total_price is not None, "Total price not displayed"
    
    # 9. Finish the purchase journey
    checkout_page.click_finish()
    time.sleep(2)
    
    # 10. Verify successful order message
    success_message = checkout_page.get_complete_message()
    expected_messages = ["Thank you for your order!", "THANK YOU FOR YOUR ORDER"]
    assert any(msg in success_message.upper() for msg in expected_messages), \
        f"Expected success message but got: {success_message}"
    
    # 11. Navigate back to products
    checkout_page.back_to_products()
    time.sleep(1)
    
    # 12. Reset App State again
    inventory_page.open_menu()
    time.sleep(1)
    inventory_page.reset_app_state()
    time.sleep(1)
    inventory_page.close_menu()
    time.sleep(1)
    
    # 13. Logout
    inventory_page.logout()