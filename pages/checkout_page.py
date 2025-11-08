from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    # Locators
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    
    @allure.step("Fill checkout information")
    def fill_checkout_information(self, first, last, postal):
        self.enter_text(self.FIRST_NAME, first)
        self.enter_text(self.LAST_NAME, last)
        self.enter_text(self.POSTAL_CODE, postal)
    
    @allure.step("Click continue button")
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
    
    @allure.step("Get all product names in checkout")
    def get_all_product_names(self):
        elements = self.find_elements(self.ITEM_NAMES)
        return [element.text for element in elements]
    
    @allure.step("Get total price")
    def get_total_price(self):
        total_text = self.get_text(self.TOTAL)
        # Extract price from "Total: $XX.XX"
        return total_text.replace("Total: ", "").strip()
    
    @allure.step("Get subtotal")
    def get_subtotal(self):
        subtotal_text = self.get_text(self.SUBTOTAL)
        return subtotal_text.replace("Item total: ", "").strip()
    
    @allure.step("Get tax amount")
    def get_tax(self):
        tax_text = self.get_text(self.TAX)
        return tax_text.replace("Tax: ", "").strip()
    
    @allure.step("Click finish button")
    def click_finish(self):
        self.click(self.FINISH_BUTTON)
    
    @allure.step("Get order complete message")
    def get_complete_message(self):
        return self.get_text(self.COMPLETE_HEADER)
    
    @allure.step("Check if order is complete")
    def is_order_complete(self):
        return self.is_element_visible(self.COMPLETE_HEADER)
    
    @allure.step("Navigate back to products")
    def back_to_products(self):
        self.click(self.BACK_HOME_BUTTON)