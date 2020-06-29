import unittest
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class SeleniumEasy(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

    def test_display_message(self):
        # wait_for_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator=id("")))
        enter_message_field = self.driver.find_element_by_xpath('//div[@class="form-group"]//input[@id="user-message"]')
        enter_message_field.send_keys('hello')

        show_message_button = self.driver.find_element_by_xpath('//button[contains(text(), "Show Message")]')
        show_message_button.click()

        your_message = self.driver.find_element_by_xpath('//span[contains(text(), "hello")]')
        assert your_message.is_displayed()

    def test_total(self):
        enter_a_field = self.driver.find_element_by_id('sum1')
        enter_a_field.send_keys('5')

        enter_b_field = self.driver.find_element_by_id('sum2')
        enter_b_field.send_keys('5')

        get_total_button = self.driver.find_element_by_xpath('//button[contains(text(), "Get Total")]')
        get_total_button.click()

        total = self.driver.find_element_by_xpath('//span[contains(text(), "10")]')
        assert total.is_displayed()


    def tearDown(self):
        self.driver.close()