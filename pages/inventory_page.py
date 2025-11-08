from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import allure
import time


class InventoryPage(BasePage):
    # Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, "a.shopping_cart_link")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_item:first-child .inventory_item_name")
    FIRST_ADD_TO_CART = (By.CSS_SELECTOR, ".inventory_item:first-child button")
    CLOSE_MENU = (By.ID, "react-burger-cross-btn")
    
    @allure.step("Open hamburger menu")
    def open_menu(self):
        try:
            self.click(self.MENU_BUTTON)
            time.sleep(1)
        except:
            print("Menu button already clicked or not found")
    
    @allure.step("Close hamburger menu")
    def close_menu(self):
        try:
            self.click(self.CLOSE_MENU)
            time.sleep(0.5)
        except:
            print("Menu already closed")
    
    @allure.step("Reset application state")
    def reset_app_state(self):
        """Reset just clicks the reset link - menu should be opened before calling this"""
        self.click(self.RESET_LINK)
        time.sleep(1)
    
    @allure.step("Logout from application")
    def logout(self):
        try:
            self.open_menu()
            time.sleep(1)
            self.click(self.LOGOUT_LINK)
        except:
            # If menu is already open
            self.click(self.LOGOUT_LINK)
    
    @allure.step("Sort products by: {sort_option}")
    def sort_products(self, sort_option):
        dropdown_element = self.find_element(self.SORT_DROPDOWN)
        select = Select(dropdown_element)
        
        if sort_option == "za":
            select.select_by_value("za")
        elif sort_option == "lohi":
            select.select_by_value("lohi")
        elif sort_option == "hilo":
            select.select_by_value("hilo")
        else:
            select.select_by_value("az")
        
        time.sleep(2)
    
    @allure.step("Add product to cart: {name}")
    def add_product_to_cart_by_name(self, name):
        xpath = f"//div[@class='inventory_item_name ' and text()='{name}']/ancestor::div[@class='inventory_item']//button"
        
        try:
            button_locator = (By.XPATH, xpath)
            element = self.find_element(button_locator, timeout=5)
            element.click()
            time.sleep(0.5)
            print(f"Successfully added {name} to cart")
        except Exception as e:
            print(f"Failed primary method for {name}: {str(e)}")
            alt_xpath = f"//div[contains(text(), '{name}')]/ancestor::div[@class='inventory_item']//button"
            try:
                self.driver.find_element(By.XPATH, alt_xpath).click()
                time.sleep(0.5)
                print(f"Successfully added {name} using alternative method")
            except Exception as e2:
                print(f"Both methods failed for {name}: {str(e2)}")
                raise
    
    @allure.step("Add first product to cart")
    def add_first_product_to_cart(self):
        element = self.find_element(self.FIRST_ADD_TO_CART)
        element.click()
        time.sleep(0.5)
    
    @allure.step("Get first product name")
    def get_first_product_name(self):
        return self.get_text(self.FIRST_PRODUCT_NAME)
    
    @allure.step("Navigate to shopping cart")
    def go_to_cart(self):
        """Navigate directly to cart page"""
        print("Navigating to cart page...")
        self.driver.get("https://www.saucedemo.com/cart.html")
        time.sleep(2)
        print(f"Current URL after navigation: {self.driver.current_url}")
    
    @allure.step("Get cart item count")
    def get_cart_count(self):
        try:
            return self.get_text(self.CART_BADGE)
        except:
            return "0"