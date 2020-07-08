import unittest
from selenium import webdriver


class TestTable(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/table-pagination-demo.html')

    # def test_table_total_rows(self):
    #     table_rows = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr')
    #     assert len(table_rows) == 13
    #
    # def test_total_row_cells(self):
    #     all_cells = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr/td')
    #     assert len(all_cells) == 91
    #
    # def test_cell_name(self):
    #     all_cell = self.driver.find_elements_by_xpath('//tbody[@id="myTable"]//tr[2]/td')
    #
    #     cell_names = []
    #     for element in all_cell:
    #         cell_names.append(element.text)
    #
    #     assert all_cell[3].text == 'Table cell'

    def test_table_heading_rows(self):
        all_heading = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]//tr/th')
        assert len(all_heading) == 7

    def test_heading_name(self):
        all_heading = self.driver.find_elements_by_xpath('//thead[@class="btn-primary"]//tr/th')
        heading_list = []
        for element in all_heading:
            heading_list.append(element.text)

        assert heading_list[5] == 'Table heading 5'

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
