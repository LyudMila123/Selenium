import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestTableFoto(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html')

    def test_first_name(self):
        get_new_user = self.driver.find_element_by_xpath('//div[@class="panel-body"]//button[@class="btn btn-default"]')
        get_new_user.click()

        first_name = self.driver.find_element_by_xpath('//*[text()[contains(.,"First")]]')
        assert first_name.is_displayed()
        last_name = self.driver.find_element_by_xpath('//*[text()[contains(.,"Last")]]')
        assert last_name.is_displayed()
        # img = self.driver.find_elements_by_xpath('')
        # assert img[0].is_displayed()

    def tearDown(self):
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()

        # first_name = self.driver.find_elements_by_xpath('//div[@id="loading"]/text()[1]')
        wait_for_first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="loading"]/text(()[1]')))
        # first_name = self.driver.find_element_by_xpath('//div[@id="loading"]/text()[1]')
        #
        # assert first_name.is_displayed()



        # list = self.driver.find_elements_by_xpath('//div[@id="loading"]')
        # print(list)
        # res = []
        # for i in list:
        #     res.append(i.text)
        # foto = self.driver.find_elements_by_xpath('//div[@id="loading"]/img[@src="https://randomuser.me/api/portraits/men/20.jpg"]')
        # # assert 'First Name' in list
        # assert foto in res
        # first_name = self.driver.find_elements_by_xpath('//div[@id="loading" and contains(text(),"First Name")]')
        # first_name = self.driver.find_elements_by_name('//div[@id="loading"]/text()[1]')


        # first_name = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/text()[1]')
        # wait_for_first_name = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(By.XPATH,//div[contains(text(),"First Name :")])
        # print(first_name)
        # last_name = self.driver.find_elements_by_xpath('//div[contains(text(),"Last Name :")]')
        # print(last_name)
        # foto = self.driver.find_elements_by_xpath('//div[@id="loading"]/img[contains(@src,"randomuser")]')
        # ('//div[@id="loading"]/img[not(contains(@src,"randomuser"))]')
        # # wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(foto))
        # list = []
        # for i in foto:
        #     list.append(i)
        # print(foto)


        # results = self.driver.find_element_by_id('//*[@id="loading"]')
        # results.find_element_by_xpath('img')
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='loading']/img[contains(@src,'randomuser')]")))
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'First Name :')]")))
        # assert results.find_element_by_xpath('img').is_displayed()
        #
        # wait.until(
        #     EC.visibility_of_element_located((By.XPATH, "//div[@id='loading']/img[contains(@src,'randomuser')]")))
        # wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'First Name :')]")))

        # wait_first_name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located)
        # foto = self.driver.find_elements_by_xpath('//div[@id="loading"]//img[@src="https://randomuser.me/api/portraits/men/11.jpg"]')

        # name_list = self.driver.find_elements_by_xpath('//div[@id="loading"]/text()')
        # my_list = []
        # for i in name_list:
        #     my_list.append(i.text)
        # print(name_list)


        # assert first_name.is_displayed()
        #
        #





