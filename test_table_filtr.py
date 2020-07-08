import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTableFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/table-search-filter-demo.html')

    #valid value in table
    # def test_table_valid(self):
    #     search_line = self.driver.find_element_by_xpath('//div[@class="panel panel-primary"]//input[@class="form-control"]')
    #     search_line.send_keys('jQuery library')
    #     search_line.click()
    #
    #     rows_filter = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]//tr[5]/td')
    #     var = self.driver.find_element_by_xpath('//table[@class="table table-hover"]//tr[5]/td[2]')
    #     if rows_filter[1] == var:
    #         assert rows_filter[1] == self.driver.find_element_by_xpath('//*[text()[contains(.,"jQuery library")]]')
    #         print('Results are found')
    #     else:
    #         print('Do it again')
    #
    # def test_table_invalid(self):
    #     search_line = self.driver.find_element_by_xpath('//div[@class="panel panel-primary"]//input[@class="form-control"]')
    #     search_line.send_keys('Function')
    #     rows = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]//tr')
    #     search_line.click()
    #
    #     rows_filter = []
    #     for i in rows:
    #         rows_filter.append(i)
    #     if rows_filter[1] == self.driver.find_elements_by_xpath('//*[text()[contains(.,"Function")]]'):
    #         assert rows_filter[1] == self.driver.find_elements_by_xpath('//*[text()[contains(.,"Function")]]')
    #         return print('Invalid value is found')
    #     else:
    #         return print('This value is invalid')
    # #
    def test_table_len(self):
        rows = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody/tr')
        print(rows)

        rows_after_filter = []
        for i in rows:
            rows_after_filter.append(i.text)
        assert len(rows_after_filter) == 7
        print(len(rows_after_filter) == 7)

    def test_input_u(self):
        search_line = self.driver.find_element_by_id('task-table-filter')
        search_line.send_keys('u')
        results = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr[not(contains(@style,"display: none;"))]')
        result_list = []
        for i in results:
            result_list.append(i.text)
        assert len(result_list) == 4

    def test_input_mi(self):
        search_line = self.driver.find_element_by_id('task-table-filter')
        search_line.send_keys('mi')
        all_results = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr[not(contains(@style,"display: none;"))]')
        search_line.click()
        # print(all_results)
        my_result = []
        for i in all_results:
            my_result.append(i.text)
        # print(my_result)
        assert 'Wireframes' in my_result[0]
        assert len(my_result) == 3

        # wait_for_all_results = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located)
        # all_results = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]//tbody/tr[@style="display: table-row;"]')
        # all_results = self.driver.find_elements_by_xpath('//table[@class="table table-hover"]/tbody/tr[(contains(@style,"display: table-row;"))]')
        # all_results = self.driver.find_elements_by_xpath('//*[@id="task-table"]/tbody/tr[@style="display: table-row;"]')
        # all_results = self.driver.find_elements_by_xpath('//*[@id="task-table"]/tbody/tr[@style="display: none;"]')


        # first_word_results = [my_result[0]]
        # print(first_word_results)
        # # for x in all_results:
        # #     first_word_results.append(x.text)
        # assert 'Wireframes' in first_word_results





        # rows = self.driver.find_elements_by_xpath('//table[@id="task-table"]//tbody/tr')
        # rows_input_u = []
        # for i in rows:
        #     rows_input_u.append(i.text)
        #
        #
        # assert len(rows_input_u) == 4


    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

