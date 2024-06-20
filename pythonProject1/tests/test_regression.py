from time import sleep
from selenium.webdriver.common.by import By

from pageObjects.cartPage import CartPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.shopPage import ShopPage
from utilities.baseClass import BaseClass


class TestEndToEnd(BaseClass):

    def test_end_to_end(self):
        shop_page = ShopPage(self.driver)               #create an instints of a class . in this case for our shop page
        shop_page.get_add_to_cart_button().click()
        shop_page.get_cart_button().click()
        shop_page.get_view_my_cart_button().click()
        cart_page = CartPage(self.driver)
        cart_page.get_add_coupon_button().click()
        cart_page.get_coupon_input_field().send_keys("Tojtech-10$")
        cart_page.get_apply_button().click()
        cart_page.get_proceed_to_checkout_button().click()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.get_country_field().send_keys("Uni")

        for country in checkout_page.get_list_of_countries():
            if country.text == "United Kingdom (UK)":
                country.click()
            break
        #
        # checkout_page.get_frames()
        # checkout_page.get_switch_frame()
        # checkout_page.get_number_of_input().click().send_keys("4242424242424242")
        # checkout_page.get_place_order()

