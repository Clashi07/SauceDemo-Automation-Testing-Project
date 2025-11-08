import pytest
import allure
from pages.login_page import LoginPage 
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time

@pytest.mark.q3
@allure.feature('Purchase Journey')
@allure.story('Performance User with Sorting')
@allure.title('Performance user purchase with Z-A sorting and price verification')
def test_performance_user_purchase_with_sorting(driver):
    # Initialize page objects
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # 1. Login
    login_page.open()
    login_page.login("performance_glitch_user", "secret_sauce")
    time.sleep(2)  # Wait for login (performance user is slower)
    
    # 2. Reset App State FIRST
    inventory_page.open_menu()
    time.sleep(1)
    inventory_page.reset_app_state()
    time.sleep(1)
    inventory_page.close_menu()
    time.sleep(1)
    
    # 3. Filter by name (Z to A)
    inventory_page.sort_products("za")
    time.sleep(2)  # Wait for sorting (performance user is slower)
    
    # 4. Verify first product name
    first_product = inventory_page.get_first_product_name()
    assert first_product == "Test.allTheThings() T-Shirt (Red)", \
        f"Expected 'Test.allTheThings() T-Shirt (Red)' but got '{first_product}'"
    
    # 5. Add first product to cart
    inventory_page.add_first_product_to_cart()
    time.sleep(1)
    
    # 6. Navigate to cart
    driver.get("https://www.saucedemo.com/cart.html")
    time.sleep(2)
    
    # Verify we're on cart page
    assert "cart.html" in driver.current_url, f"Expected cart page but got {driver.current_url}"
    
    # 7. Proceed to checkout
    cart_page.proceed_to_checkout()
    time.sleep(2)
    
    # 8. Fill checkout information
    checkout_page.fill_checkout_information("Jane", "Smith", "54321")
    checkout_page.click_continue()
    time.sleep(2)
    
    # 9. Verify all product names on final checkout page
    displayed_products = checkout_page.get_all_product_names()
    assert first_product in displayed_products, \
        f"{first_product} not found in checkout page"
    
    # 10. Verify total price
    total_price = checkout_page.get_total_price()
    assert total_price is not None, "Total price not displayed"
    
    # 11. Finish purchase
    checkout_page.click_finish()
    time.sleep(2)
    
    # 12. Verify successful order message
    success_message = checkout_page.get_complete_message()
    expected_messages = ["Thank you for your order!", "THANK YOU FOR YOUR ORDER"]
    assert any(msg in success_message.upper() for msg in expected_messages), \
        f"Expected success message but got: {success_message}"
    
    # 13. Navigate back to products
    checkout_page.back_to_products()
    time.sleep(1)
    
    # 14. Reset App State again
    inventory_page.open_menu()
    time.sleep(1)
    inventory_page.reset_app_state()
    time.sleep(1)
    inventory_page.close_menu()
    time.sleep(1)
    
    # 15. Logout
    inventory_page.logout()