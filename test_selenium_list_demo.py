import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class SeleniumListDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html')
        self.sourch_line = Select(self.driver.find_element_by_id('select-demo'))

    def test_before_click_select(self):
        line_before_click_select = self.driver.find_element_by_xpath('//*[text()[contains(.,"Please select")]]')
        assert line_before_click_select.is_displayed()

    def test_select_list_demo(self):
        list_demo = self.driver.find_elements_by_xpath('//*[@id="select-demo"]/option')
        # print(list_demo)
    #     включено 8 элементов, в том числе и первый в списке - "Please select", остальные - дни недели

        sunday = list_demo[1].click()
        result_sunday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Sunday")]]')
        assert result_sunday.is_displayed()

        monday = list_demo[2].click()
        result_monday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Monday")]]')
        assert result_sunday.is_displayed()

        tuesday = list_demo[3].click()
        result_tuesday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Tuesday")]]')
        assert result_tuesday.is_displayed()

        wednesday = list_demo[4].click()
        result_wednesday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Wednesday")]]')
        assert result_wednesday.is_displayed()

        thursday = list_demo[5].click()
        result_thursday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Thursday")]]')
        assert result_thursday.is_displayed()

        friday = list_demo[6].click()
        result_friday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Friday")]]')
        assert result_friday.is_displayed()

        saturday = list_demo[7].click()
        result_saturday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Saturday")]]')
        assert result_saturday.is_displayed()

    def test_before_click_first_selected(self):
        button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
        button_first_selected.click()
        result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : undefined")]]')
        assert result_message.is_displayed()

    def test_first_selected(self):
        list_first_selected = self.driver.find_elements_by_xpath('//*[@id="multi-select"]/option')
        button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')

        california = list_first_selected[0].click()
        button_first_selected.click()
        result_california = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : California")]]')
        assert result_california.is_displayed()

        florida = list_first_selected[1].click()
        button_first_selected.click()
        result_florida = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Florida")]]')
        assert result_florida.is_displayed()

        new_jersey = list_first_selected[2].click()
        button_first_selected.click()
        result_new_jersey = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : New Jersey")]]')
        assert result_new_jersey.is_displayed()

        new_york = list_first_selected[3].click()
        button_first_selected.click()
        result_new_york = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : New York")]]')
        assert result_new_york.is_displayed()

        ohio = list_first_selected[4].click()
        button_first_selected.click()
        result_ohio = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Ohio")]]')
        assert result_ohio.is_displayed()

        texas = list_first_selected[5].click()
        button_first_selected.click()
        result_texas = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Texas")]]')
        assert result_texas.is_displayed()

        pennsylvania = list_first_selected[6].click()
        button_first_selected.click()
        result_pennsylvania = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Pennsylvania")]]')
        assert result_pennsylvania.is_displayed()

        washington = list_first_selected[7].click()
        button_first_selected.click()
        result_washington = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Washington")]]')
        assert result_washington.is_displayed()

    def test_before_click_get_all(self):
        button_get_all_selected = self.driver.find_element_by_xpath('//*[@id="printAll"]')
        button_get_all_selected.click()
        result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : ")]]')
        assert result_message.is_displayed()

    def test_get_all_selected(self):
        list_get_all_selected = self.driver.find_elements_by_xpath('//*[@id="multi-select"]/option')
        button_get_all_selected = self.driver.find_element_by_xpath('//*[@id="printAll"]')

        california = list_get_all_selected[0].click()
        button_get_all_selected.click()
        result_california = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : California")]]')
        assert result_california.is_displayed()

        florida = list_get_all_selected[1].click()
        button_get_all_selected.click()
        result_florida = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Florida")]]')
        assert result_florida.is_displayed()

        new_jersey = list_get_all_selected[2].click()
        button_get_all_selected.click()
        result_new_jersey = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : New Jersey")]]')
        assert result_new_jersey.is_displayed()

        new_york = list_get_all_selected[3].click()
        button_get_all_selected.click()
        result_new_york = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : New York")]]')
        assert result_new_york.is_displayed()

        ohio = list_get_all_selected[4].click()
        button_get_all_selected.click()
        result_ohio = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Ohio")]]')
        assert result_ohio.is_displayed()

        texas = list_get_all_selected[5].click()
        button_get_all_selected.click()
        result_texas = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Texas")]]')
        assert result_texas.is_displayed()

        pennsylvania = list_get_all_selected[6].click()
        button_get_all_selected.click()
        result_pennsylvania = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Pennsylvania")]]')
        assert result_pennsylvania.is_displayed()

        washington = list_get_all_selected[7].click()
        button_get_all_selected.click()
        result_washington = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Washington")]]')
        assert result_washington.is_displayed()

    def test_select_sunday(self):
        self.sourch_line.select_by_visible_text('Sunday')
        assert 'Day selected :- Sunday' in self.driver.page_source

    def test_select_monday(self):
        self.sourch_line.select_by_visible_text('Monday')
        assert 'Day selected :- Monday' in self.driver.page_source

    def test_select_tuesday(self):
        self.sourch_line.select_by_visible_text('Tuesday')
        assert 'Day selected :- Tuesday' in self.driver.page_source

    def test_select_wednesday(self):
        self.sourch_line.select_by_visible_text('Wednesday')
        assert 'Day selected :- Wednesday' in self.driver.page_source

    def test_select_thursday(self):
        self.sourch_line.select_by_visible_text('Thursday')
        assert 'Day selected :- Thursday' in self.driver.page_source

    def test_select_friday(self):
        self.sourch_line.select_by_visible_text('Friday')
        assert 'Day selected :- Friday' in self.driver.page_source

    def test_select_saturday(self):
        self.sourch_line.select_by_visible_text('Saturday')
        assert 'Day selected :- Saturday' in self.driver.page_source




    # def test_select_sunday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Sunday')
    #     line.click()
    #     result_sunday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Sunday")]]')
    #     assert result_sunday.is_displayed()
    #
    # def test_select_monday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Monday')
    #     line.click()
    #     result_monday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Monday")]]')
    #     assert result_monday.is_displayed()
    #
    # def test_select_tuesday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Tuesday')
    #     line.click()
    #     result_tuesday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Tuesday")]]')
    #     assert result_tuesday.is_displayed()
    #
    # def test_select_wednesday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Wednesday')
    #     line.click()
    #     result_wednesday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Wednesday")]]')
    #     assert result_wednesday.is_displayed()
    #
    # def test_select_thursday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Thursday')
    #     line.click()
    #     result_thursday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Thursday")]]')
    #     assert result_thursday.is_displayed()
    #
    # def test_select_friday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Friday')
    #     line.click()
    #     result_friday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Friday")]]')
    #     assert result_friday.is_displayed()

    # def test_select_saturday_second(self):
    #     line = self.driver.find_element_by_id('select-demo')
    #     line.send_keys('Saturday')
    #     line.click()
    #     result_saturday = self.driver.find_element_by_xpath('//*[text()[contains(.,"Day selected :- Saturday")]]')
    #     assert result_saturday.is_displayed()
    #
    # def test_california_first(self):
    #     button_calufornia = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[1]')
    #     button_calufornia.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : California")]]')
    #     assert result_message.is_displayed()
    #
    # def test_florida_first(self):
    #     button_florida = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[2]')
    #     button_florida.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Florida")]]')
    #     assert result_message.is_displayed()
    #
    # def test_new_jersey_first(self):
    #     button_new_jersey = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[3]')
    #     button_new_jersey.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : New Jersey")]]')
    #     assert result_message.is_displayed()
    #
    # def test_new_york_first(self):
    #     button_new_tork = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[4]')
    #     button_new_tork.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : New York")]]')
    #     assert result_message.is_displayed()
    #
    # def test_ohio_first(self):
    #     button_ohio = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[5]')
    #     button_ohio.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Ohio")]]')
    #     assert result_message.is_displayed()
    #
    # def test_texas_first(self):
    #     button_texas = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[6]')
    #     button_texas.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Texas")]]')
    #     assert result_message.is_displayed()
    #
    # def test_pennsylvania_first(self):
    #     button_pennsylvania = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[7]')
    #     button_pennsylvania.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Pennsylvania")]]')
    #     assert result_message.is_displayed()
    #
    # def test_washington_first(self):
    #     button_washington = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[8]')
    #     button_washington.click()
    #     button_first_selected = self.driver.find_element_by_xpath('//*[@id="printMe"]')
    #     button_first_selected.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"First selected option is : Washington")]]')
    #     assert result_message.is_displayed()
    #
    # def test_california_get_all(self):
    #     button_calufornia = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[1]')
    #     button_calufornia.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : California")]]')
    #     assert result_message.is_displayed()
    #
    # def test_florida_get_all(self):
    #     button_florida = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[2]')
    #     button_florida.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Florida")]]')
    #     assert result_message.is_displayed()
    #
    # def test_new_jersey_get_all(self):
    #     button_new_jersey = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[3]')
    #     button_new_jersey.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : New Jersey")]]')
    #     assert result_message.is_displayed()
    #
    # def test_new_york_get_all(self):
    #     button_new_york = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[4]')
    #     button_new_york.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : New York")]]')
    #     assert result_message.is_displayed()
    #
    # def test_ohio_get_all(self):
    #     button_ohio = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[5]')
    #     button_ohio.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Ohio")]]')
    #     assert result_message.is_displayed()
    #
    # def test_texas_get_all(self):
    #     button_texas = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[6]')
    #     button_texas.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Texas")]]')
    #     assert result_message.is_displayed()
    #
    # def test_pennsylvania_get_all(self):
    #     button_pennsylvania = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[7]')
    #     button_pennsylvania.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Pennsylvania")]]')
    #     assert result_message.is_displayed()
    #
    # def test_washington_get_all(self):
    #     button_washington = self.driver.find_element_by_xpath('//*[@id="multi-select"]/option[8]')
    #     button_washington.click()
    #     button_get_all = self.driver.find_element_by_xpath('//*[@id="printAll"]')
    #     button_get_all.click()
    #     result_message = self.driver.find_element_by_xpath('//*[text()[contains(.,"Options selected are : Washington")]]')
    #     assert result_message.is_displayed()

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()