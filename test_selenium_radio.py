import unittest
from selenium import webdriver


class SeleniumEasyRadioButton(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')

    def test_radio_button_demo_male(self):
        radio_button_demo_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="optradio"]')
        radio_button_demo_male.click()
        checked_value = self.driver.find_element_by_id('buttoncheck')
        checked_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="radiobutton"]')
        assert message.is_displayed(), "Radio button 'Male' is checked"

    def test_radio_button_demo_female(self):
        radio_button_demo_female = self.driver.find_element_by_xpath('//input[@value="Female"][@name="optradio"]')
        radio_button_demo_female.click()
        checked_value = self.driver.find_element_by_id('buttoncheck')
        checked_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="radiobutton"]')
        assert message.is_displayed(), "Radio button 'Female' is checked"

    def test_radio_button_demo_for(self):
        radio_button_demo = self.driver.find_elements_by_xpath('//div[@class="panel-body"]/label[@class="radio-inline"]')
        radio_demo_list = []

        for element in radio_button_demo:
            radio_demo_list.append(element)

        radio_demo_male = radio_demo_list[0].click()
        checked_value = self.driver.find_element_by_id('buttoncheck')
        checked_value.click()
        message_male = self.driver.find_element_by_xpath('//p[@class="radiobutton"]')
        assert message_male.is_displayed(), "Radio button 'Male' is checked"

        radio_demo_female = radio_demo_list[1].click()
        checked_value = self.driver.find_element_by_id('buttoncheck')
        checked_value.click()
        message_female = self.driver.find_element_by_xpath('//p[@class="radiobutton"]')
        assert message_female.is_displayed(), "Radio button 'Female' is checked"

    def test_group_radio_buttons_demo_male_0_to_5(self):
        group_radio_button_demo_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        group_radio_button_demo_male.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="0 - 5"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 0 - 5'

    def test_group_radio_buttons_demo_male_5_to_15(self):
        group_radio_button_demo_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        group_radio_button_demo_male.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="5 - 15"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 5 - 15'

    def test_group_radio_buttons_demo_male_15_to_50(self):
        group_radio_button_demo_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        group_radio_button_demo_male.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="15 - 50"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 15 - 50'

    def test_group_radio_buttons_demo_female_0_to_5(self):
        group_radio_button_demo_female = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        group_radio_button_demo_female.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="0 - 5"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 0 - 5'

    def test_group_radio_buttons_demo_female_5_to_15(self):
        group_radio_button_demo_female = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        group_radio_button_demo_female.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="5 - 15"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 5 - 15'

    def test_group_radio_buttons_demo_female_15_to_50(self):
        group_radio_button_demo_female = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        group_radio_button_demo_female.click()
        age_group_radio = self.driver.find_element_by_xpath('//input[@value="15 - 50"][@name="ageGroup"]')
        age_group_radio.click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 15 - 50'

    def test_group_radio_buttons_for(self):
        group_radio_buttons = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//input[@name="gender"]')
        group_radio_buttons_list = []

        for element in group_radio_buttons:
            group_radio_buttons_list.append(element)

        age_group_radio_buttons = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//input[@name="ageGroup"]')
        age_group_radio_buttons_list = []

        for number in age_group_radio_buttons:
            age_group_radio_buttons_list.append(number)

        group_radio_buttons_list_male = group_radio_buttons_list[0].click()
        age_group_0_5 = age_group_radio_buttons_list[0].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 0 - 5'

        group_radio_buttons_list_male = group_radio_buttons_list[0].click()
        age_group_5_15 = age_group_radio_buttons_list[1].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 5 - 15'

        group_radio_buttons_list_male = group_radio_buttons_list[0].click()
        age_group_15_50 = age_group_radio_buttons_list[2].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Male Age group: 15 - 50'

        group_radio_buttons_list_female = group_radio_buttons_list[1].click()
        age_group_0_5 = age_group_radio_buttons_list[0].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 0 - 5'

        group_radio_buttons_list_female = group_radio_buttons_list[1].click()
        age_group_5_15 = age_group_radio_buttons_list[1].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 5 - 15'

        group_radio_buttons_list_female = group_radio_buttons_list[1].click()
        age_group_15_50 = age_group_radio_buttons_list[2].click()
        get_value = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@onclick="getValues();"]')
        get_value.click()
        message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert message.is_displayed(), 'Sex : Female Age group: 15 - 50'

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

