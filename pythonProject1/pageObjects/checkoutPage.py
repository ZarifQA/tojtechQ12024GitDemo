import self
import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.conftest import driver


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    country_field = (By.CSS_SELECTOR, "#components-form-token-input-0")
    list_of_countries = (By.CSS_SELECTOR, ".components-form-token-field__suggestion")
    number_of_input = (By.CSS_SELECTOR, "#Field-numberInput")
    place_order = (By.XPATH, "//span[text()='Place Order']")
    # frames = (By.TAG_NAME, "iframe")
    # switch_frame = driver.switch_to.frame(frames)

    def get_country_field(self):
        return self.driver.find_element(*CheckoutPage.country_field)

    def get_list_of_countries(self):
        return self.driver.find_elements(*CheckoutPage.list_of_countries)

    # def get_frames(self):
    #     return self.driver.find_element(*CheckoutPage.frames)
    #
    # def get_switch_frame(self):
    #     return self.driver.switch_to.frame(frames[1])


    def get_number_of_input(self):
        return self.driver.find_element(*CheckoutPage.number_of_input)

    def get_place_order(self):
        return self.driver.find_element(*CheckoutPage.place_order)







    # self.driver.find_element(By.CSS_SELECTOR, "#components-form-token-input-0").send_keys("Uni")
    #
    # list_of_countries = self.driver.find_elements(By.CSS_SELECTOR, ".components-form-token-field__suggestion")

    # frame_element = self.driver.find_elements(By.TAG_NAME, "iframe")
    # self.driver.switch_to.frame(frame_element[1])
    # sleep(2)
    # self.driver.find_element(By.CSS_SELECTOR, "#Field-numberInput").send_keys("4242424242424242")
    # sleep(2)
    # self.driver.switch_to.default_content()
    # sleep(2)
    # self.driver.find_element(By.XPATH, "//span[text()='Place Order']").click()
    # sleep(4)
    # self.driver.quit()