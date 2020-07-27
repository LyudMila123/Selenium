import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestGlobalsqa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('http://www.globalsqa.com/demo-site/')

# убедиться что есть такая закладка - работает
    def test_tabs_simple_accordion(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]')))
        simple_accordion = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]')
        simple_accordion.click()
        assert simple_accordion.is_displayed()

# убедиться что есть такая закладка - работает
    def test_tabs_re_size_accordion(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')))
        re_size_accordion = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')
        re_size_accordion.click()
        assert re_size_accordion.is_displayed()

# убедиться что есть такая закладка - работает
    def test_tabs_toggle_icons(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]')))
        toggle_icons = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]')
        toggle_icons.click()
        assert toggle_icons.is_displayed()

# сообщение есть и его можно закрыть - работает
    def test_tabs_message_closed(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]')))
        simple_accordion = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]')
        simple_accordion.click()
        message = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]')
        assert message.is_displayed()
        message_closed = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# сообщение есть и его можно закрыть - работает
    def test_re_size_message_closed(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')))
        re_size_accordion = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')
        re_size_accordion.click()
        message = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]')
        assert message.is_displayed()
        message_closed = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# сообщение есть и его можно закрыть - работает
    def test_toogle_message_closed(self):
        tabs = self.driver.find_element_by_xpath('//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]')
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')))
        re_size_accordion = self.driver.find_element_by_xpath('//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]')
        re_size_accordion.click()
        message = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]')
        assert message.is_displayed()
        # wait_for_message_closed = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')))
        message_closed = self.driver.find_element_by_xpath('//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]')
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# есть три закладки
    def test_tooltip(self):
        tooltip = self.driver.find_element_by_xpath('//div[@class="price_column "]//a[@href="http://www.globalsqa.com/demo-site/tooltip"]')
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()
        assert image_based.is_displayed()
        wait_tooltip_video = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')))
        video_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')
        video_based.click()
        assert video_based.is_displayed()
        wait_tooltip_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')))
        forms_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')
        forms_based.click()
        assert forms_based.is_displayed()

# сообщение есть и его можно закрыть
    def test_tooltip_message_image(self):
        tooltip = self.driver.find_element_by_xpath('//div[@class="price_column "]//a[@href="http://www.globalsqa.com/demo-site/tooltip"]')
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()
        message_image = self.driver.find_element_by_xpath('//div[@rel-title="Image Based"]//div[@class="attention closable"]')
        assert message_image.is_displayed()
        message_image_close = self.driver.find_element_by_xpath('//div[@rel-title="Image Based"]//a[@class="close_img"]')
        message_image_close.click()
        message_image_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_image_not.is_displayed()

    def test_tooltip_message_video(self):
        tooltip = self.driver.find_element_by_xpath('//div[@class="price_column "]//a[@href="http://www.globalsqa.com/demo-site/tooltip"]')
        tooltip.click()
        wait_tooltip_video = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')))
        video_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')
        video_based.click()
        message_video = self.driver.find_element_by_xpath('//div[@rel-title="Video Based"]//div[@class="attention closable"]')
        assert message_video.is_displayed()
        message_video_close = self.driver.find_element_by_xpath('//div[@rel-title="Video Based"]//a[@class="close_img"]')
        message_video_close.click()
        message_video_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_video_not.is_displayed()

    def test_tooltip_message_forms(self):
        tooltip = self.driver.find_element_by_xpath('//div[@class="price_column "]//a[@href="http://www.globalsqa.com/demo-site/tooltip"]')
        tooltip.click()
        wait_tooltip_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')))
        forms_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')
        forms_based.click()
        message_forms = self.driver.find_element_by_xpath('//div[@rel-title="Forms Based"]//div[@class="attention closable"]')
        assert message_forms.is_displayed()
        message_forms_close = self.driver.find_element_by_xpath('//div[@rel-title="Forms Based"]//a[@class="close_img"]')
        message_forms_close.click()
        message_forms_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_forms_not.is_displayed()

# закладка alert_box кнопка try_it - работает
    def test_alert_box_simple_try_it(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-labelledby="tab_item-0"]//button')))
        simple_alert_box = self.driver.find_element_by_xpath('//li[@id="Simple Alert Box"]')
        simple_alert_box.click()
        try_it_simple = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-0"]//button')
        try_it_simple.click()
        assert try_it_simple.is_displayed()

    def test_alertbox_confirmation_box_try_it(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Confirmation Box"]')))
        confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
        confirmation_box.click()
        try_it_confirmation = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-1"]//button')
        try_it_confirmation.click()
        assert try_it_confirmation.is_displayed()

    def test_alertbox_prompt_box_try_it(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Prompt Box"]')))
        prompt_box = self.driver.find_element_by_xpath('//li[@id="Prompt Box"]')
        prompt_box.click()
        try_it_prompt_box = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-2"]//button')
        try_it_prompt_box.click()
        assert try_it_prompt_box.is_displayed()

# закладка alert_box убедиться что есть три закладки - работает
    def test_alert_box_simple(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-labelledby="tab_item-0"]//button')))
        simple_alert_box = self.driver.find_element_by_xpath('//li[@id="Simple Alert Box"]')
        simple_alert_box.click()
        assert simple_alert_box.is_displayed()

    def test_alertbox_confirmation_box(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Confirmation Box"]')))
        confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
        confirmation_box.click()
        assert confirmation_box.is_displayed()

    def test_alertbox_prompt_box(self):
        alertbox = self.driver.find_element_by_xpath('//li[@class="price_footer"]/a[@href="http://www.globalsqa.com/demo-site/alertbox/"]')
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Prompt Box"]')))
        prompt_box = self.driver.find_element_by_xpath('//li[@id="Prompt Box"]')
        prompt_box.click()
        assert prompt_box.is_displayed()

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
