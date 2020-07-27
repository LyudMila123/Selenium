import unittest
from selenium import webdriver


class TestTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('http://www.practiceselenium.com/')

    def test_herbal_tea(self):
        list_see_collections = self.driver.find_elements_by_xpath('//div[@class="wsb-element-button"]//span')
        list_see_collections[0].click()
        button_check_out = self.driver.find_element_by_xpath('//div[@id="wsb-element-00000000-0000-0000-0000-000451955160"]//span[@class="button-content wsb-button-content"]')
        button_check_out.click()
        e_mail = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="email"]')
        e_mail.send_keys('lyudmilachunihina@gmail.com')
        name = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="name"]')
        name.send_keys('Lyudmila')
        address = self.driver.find_element_by_xpath('//div[@class="container"]//textarea[@id="address"]')
        address.send_keys('Kharkov')
        cart_type = self.driver.find_elements_by_xpath('//*[@id="card_type"]/option')
        cart_type[1].click()
        card_number = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="card_number"]')
        card_number.send_keys('45671234')
        card_holder = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="cardholder_name"]')
        card_holder.send_keys('lyuda')
        verification_code = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="verification_code"]')
        verification_code.click()
        button_place_order = self.driver.find_element_by_xpath('//div[@class="container"]//input[@id="verification_code"]')
        button_place_order.click()
        assert button_place_order.is_displayed()

    def test_lets_talk_tea(self):
        lets_talk_tea = self.driver.find_element_by_xpath('//ul[@class="wsb-navigation-rendered-top-level-menu "]//a[@href="let-s-talk-tea.html"]')
        lets_talk_tea.click()
        name = self.driver.find_element_by_xpath('//div[@class="form-body"]//input[@name="name"]')
        name.send_keys('lyudmila')
        email = self.driver.find_element_by_xpath('//div[@class="form-body"]//input[@name="email"]')
        email.send_keys('lyudmilachunihina@gmail.com')
        subject = self.driver.find_element_by_xpath('//div[@class="form-body"]//input[@name="subject"]')
        subject.send_keys('tea')
        message = self.driver.find_element_by_xpath('//div[@class="form-body"]//textarea[@name="message"]')
        message.send_keys('I like tea')
        submit = self.driver.find_element_by_xpath('//div[@class="form-body"]//input[@value="Submit"]')
        submit.click()
        assert submit.is_displayed()


    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()