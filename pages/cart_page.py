from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import time


class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    
    @allure.step("Get all product names in cart")
    def get_product_names(self):
        elements = self.find_elements(self.ITEM_NAMES)
        return [element.text for element in elements]
    
    @allure.step("Get all product prices in cart")
    def get_product_prices(self):
        elements = self.find_elements(self.ITEM_PRICES)
        return [element.text for element in elements]
    
    @allure.step("Proceed to checkout")
    def proceed_to_checkout(self):
        # Check if we're already on checkout page
        current_url = self.driver.current_url
        print(f"Current URL before checkout click: {current_url}")
        
        if "checkout" in current_url:
            print("Already on checkout page, skipping button click")
            return
        
        if "cart.html" not in current_url:
            print("Not on cart page, navigating there first")
            self.driver.get("https://www.saucedemo.com/cart.html")
            time.sleep(2)
        
        # Verify we have items
        try:
            items = self.driver.find_elements(*self.CART_ITEMS)
            print(f"Number of items in cart: {len(items)}")
        except Exception as e:
            print(f"Error checking cart items: {e}")
        
        # Click checkout button
        print("Clicking checkout button...")
        self.click(self.CHECKOUT_BUTTON)
        time.sleep(1)
        print(f"After checkout click, URL is: {self.driver.current_url}")