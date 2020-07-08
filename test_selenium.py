import unittest
from selenium import webdriver


class SeleniumEasyHomeTask(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

    def test_single_checkbox_demo(self):
        get_click_on_this_check_box = self.driver.find_element_by_id('isAgeSelected')
        get_click_on_this_check_box.click()

        your_message = self.driver.find_element_by_id('txtAge')
        assert your_message.is_displayed()

    def test_multiple_checkbox_demo_options(self):
        get_click_on_option_first = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 1")]]')
        get_click_on_option_first.click()

        get_click_on_option_second = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 2")]]')
        get_click_on_option_second.click()

        get_click_on_option_third = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 3")]]')
        get_click_on_option_third.click()

        get_click_on_option_third = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 4")]]')
        get_click_on_option_third.click()

        button_uncheck_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert button_uncheck_all.is_displayed()

    def test_on_uncheck_all(self):
        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        elements = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
        get_click_on_check_all.click()
        elements.is_displayed()
        assert elements.is_displayed()

    def test_check_change_uncheck_all_option_first(self):
        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        uncheck_all = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
        get_click_on_check_all.click()
        uncheck_all.is_displayed()
        get_click_on_option_first = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 1")]]')
        get_click_on_option_first.click()
        check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert check_all.is_displayed()

    def test_check_change_uncheck_all_option_second(self):
        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        uncheck_all = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
        get_click_on_check_all.click()
        uncheck_all.is_displayed()
        get_click_on_option_first = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 2")]]')
        get_click_on_option_first.click()
        check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert check_all.is_displayed()

    def test_check_change_uncheck_all_option_third(self):
        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        uncheck_all = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
        get_click_on_check_all.click()
        uncheck_all.is_displayed()
        get_click_on_option_first = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 3")]]')
        get_click_on_option_first.click()
        check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert check_all.is_displayed()

    def test_check_change_uncheck_all_option_forth(self):
        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        uncheck_all = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
        get_click_on_check_all.click()
        uncheck_all.is_displayed()
        get_click_on_option_first = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 4")]]')
        get_click_on_option_first.click()
        check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert check_all.is_displayed()

#variant 2

    def test_multiple_variant_two(self):
        button_check_all = self.driver.find_element_by_id('check1')
        button_check_all.click()

        click_option_one = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 1")]]').is_selected()
        click_option_two = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 2")]]').is_selected()
        click_option_three = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 3")]]').is_selected()
        click_option_four = self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 4")]]').is_selected()

        show_button = button_check_all.get_attribute('value')

        if self.driver.find_element_by_xpath('//*[text()[contains(.,"Option 1")]]').click():
            return button_check_all

    def test_multiple_for(self):
        checkboxes = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//input[@class="cb1-element"]')
        checkboxes_list = []

        for element in checkboxes:
            checkboxes_list.append(element)

        option_one = checkboxes_list[0].click()
        option_two = checkboxes_list[1].click()
        option_three = checkboxes_list[2].click()
        option_four = checkboxes_list[3].click()
        button_uncheck_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
        assert button_uncheck_all.is_displayed()

    # def test_multiple_for_all(self):
    #     get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="btn btn-primary"]')
    #     show_button = get_click_on_check_all.get_attribute('value')

    def test_multiple_for_option(self):
        checkboxes = self.driver.find_elements_by_xpath('//div[@class="panel-body"]//input[@class="cb1-element"]')
        checkboxes_list = []

        for element in checkboxes:
            checkboxes_list.append(element)

        get_click_on_check_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@value="Check All"]')
        get_click_on_check_all.click()
        get_click_on_uncheck_all = self.driver.find_element_by_xpath('//div[@class="panel panel-default"]//input[@value="Uncheck All"]')
        get_click_on_check_all = get_click_on_uncheck_all
        if checkboxes_list[0].click():
            # return get_click_on_check_all
            assert get_click_on_check_all.is_displayed()
        elif checkboxes_list[1].click():
            # return get_click_on_check_all
            assert get_click_on_check_all.is_displayed()
        elif checkboxes_list[2].click():
            # return get_click_on_check_all
            assert get_click_on_check_all.is_displayed()
        elif checkboxes_list[3].click():
            # return get_click_on_check_all
            assert get_click_on_check_all.is_displayed()
        else:
            return 'There are no options'

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()


    #
    #     x = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
    #     for
    #
    #
    #         i in get_click_on_check_all:
    #
    #         get_click_on_check_all.is_displayed()
    #             = self.driver.find_element_by_xpath('//*[text()[contains(.,"Uncheck All")]]')
    #     else:
    #         get_click_on_check_all = self.driver.find_element_by_id('id="check1"')
    #
    #     enter_button_of_options = self.driver.find_elements_by_xpath('//*[text()[contains(.,"Option")]]')
    #     assert enter_button_of_options.is_displyed()
    #
    #    #
    #     # self.options = self.driver.find_elements_by_xpath('//div[contains(@class="panel panel-default"]//input[@class="cb1-element"]')
    #     # for i in self.options:
    #     #     get_click_
    #     #     get_click_on_option_first.click()
    #
    #     # get_click_on_option_first = self.driver.find_elements_by_xpath('//div[contains(@class="panel panel-default"]//input[@class="cb1-element"]')
    #
        # find_element_by_xpath('//div[@class="panel panel-default"]//input[@class="cb1-element"]')