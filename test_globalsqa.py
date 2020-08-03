import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from datetime import time
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException

class TestGlobalsqa(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'E:\ui_driver/chromedriver')
        self.url = self.driver.get('http://www.globalsqa.com/demo-site/')

# TABS

# убедиться что есть такая закладка - работает

    def test_tabs_simple_accordion(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH,'//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()
        assert simple_accordion.is_displayed()

# убедиться что есть такая закладка - работает

    def test_tabs_re_size_accordion(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        re_size_accordion.click()
        assert re_size_accordion.is_displayed()

# убедиться что есть такая закладка - работает

    def test_tabs_toggle_icons(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toggle_icons = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toggle_icons.click()
        assert toggle_icons.is_displayed()

# сообщение есть и его можно закрыть - работает

    def test_tabs_message_closed(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()
        message = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]'
        )
        assert message.is_displayed()
        message_closed = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]'
        )
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# сообщение есть и его можно закрыть - работает

    def test_re_size_message_closed(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//ul[@class="resp-tabs-list "]//li[@id="Re-Size Accordion"]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//ul[@class="resp-tabs-list "]//li[@id="Re-Size Accordion"]'
        )
        re_size_accordion.click()
        message = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]'
        )
        assert message.is_displayed()
        message_closed = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]'
        )
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# сообщение есть и его можно закрыть - работает

    def test_toogle_message_closed(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        toogle_accordion.click()
        message = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//div[@class="attention closable"]'
        )
        assert message.is_displayed()
        message_closed = self.driver.find_element_by_xpath(
            '//div[@class="single_tab_div resp-tab-content resp-tab-content-active"]//a[@class="close_img"]'
        )
        message_closed.click()
        message_not = self.driver.find_element_by_css_selector('#post-2654 .resp-tab-content-active > div')
        assert message_not.is_displayed()

# секции закладки 1 -  работают

    def test_tabs_simple_section_one(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()

        section_one_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[1]/p/iframe')
        self.driver.switch_to.frame(section_one_iframe)
        wait_section_one = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@id="accordion"]//span[@class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-s"]'
        )))
        section_one = self.driver.find_element_by_xpath(
            '//div[@id="accordion"]//span[@class="ui-accordion-header-icon ui-icon ui-icon-triangle-1-s"]'
        )
        section_one.click()
        assert section_one.is_displayed()

    def test_tabs_simple_section_two(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()

        section_two_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[1]/p/iframe')
        self.driver.switch_to.frame(section_two_iframe)
        wait_section_two = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-3"]/span'
        )))
        section_two = self.driver.find_element_by_xpath('//h3[@id="ui-id-3"]/span')
        section_two.click()
        assert section_two.is_displayed()

    def test_tabs_simple_section_three(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()

        section_three_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[1]/p/iframe')
        self.driver.switch_to.frame(section_three_iframe)
        wait_section_three = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-5"]/span'
        )))
        section_three = self.driver.find_element_by_xpath('//h3[@id="ui-id-5"]/span')
        section_three.click()
        assert section_three.is_displayed()

    def test_tabs_simple_section_four(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_simple = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )))
        simple_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Simple Accordion")]'
        )
        simple_accordion.click()

        section_four_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[1]/p/iframe')
        self.driver.switch_to.frame(section_four_iframe)
        wait_section_four = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-7"]/span'
        )))
        section_four = self.driver.find_element_by_xpath('//h3[@id="ui-id-7"]/span')
        section_four.click()
        assert section_four.is_displayed()

    def test_tabs_re_size_section_one(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        re_size_accordion.click()

        section_one_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[2]/p[1]/iframe')
        self.driver.switch_to.frame(section_one_iframe)
        wait_section_one = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//h3[@id="ui-id-1"]//span')))

        section_one = self.driver.find_element_by_xpath('//h3[@id="ui-id-1"]/span')
        section_one.click()
        assert section_one.is_displayed()

    def test_tabs_re_size_section_two(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        re_size_accordion.click()

        section_two_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[2]/p[1]/iframe')
        self.driver.switch_to.frame(section_two_iframe)
        wait_section_two = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-3"]//span'
        )))

        section_two = self.driver.find_element_by_xpath('//h3[@id="ui-id-3"]//span')
        section_two.click()
        assert section_two.is_displayed()

    def test_tabs_re_size_section_three(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        re_size_accordion.click()

        section_three_iframe = self.driver.find_element_by_xpath(
            '//*[@id="post-2654"]/div[2]/div/div/div[2]/p[1]/iframe'
        )
        self.driver.switch_to.frame(section_three_iframe)
        wait_section_three = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-5"]//span'
        )))

        section_three = self.driver.find_element_by_xpath('//h3[@id="ui-id-5"]//span')
        section_three.click()
        assert section_three.is_displayed()

    def test_tabs_re_size_section_four(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_re_size = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )))
        re_size_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Re-Size Accordion")]'
        )
        re_size_accordion.click()

        section_four_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[2]/p[1]/iframe')
        self.driver.switch_to.frame(section_four_iframe)
        wait_section_four = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-7"]//span'
        )))

        section_four = self.driver.find_element_by_xpath('//h3[@id="ui-id-7"]//span')
        section_four.click()
        assert section_four.is_displayed()

    def test_tabs_toogle_section_one(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toogle_accordion.click()

        section_one_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(section_one_iframe)
        wait_section_one = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-1"]//span'
        )))

        section_one = self.driver.find_element_by_xpath('//h3[@id="ui-id-1"]//span')
        section_one.click()
        assert section_one.is_displayed()

    def test_tabs_toogle_section_two(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toogle_accordion.click()

        section_two_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(section_two_iframe)
        wait_section_two = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-3"]//span'
        )))

        section_two = self.driver.find_element_by_xpath('//h3[@id="ui-id-3"]//span')
        section_two.click()
        assert section_two.is_displayed()

    def test_tabs_toogle_section_three(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toogle_accordion.click()

        section_three_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(section_three_iframe)
        wait_section_three = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-5"]//span'
        )))

        section_three = self.driver.find_element_by_xpath('//h3[@id="ui-id-5"]//span')
        section_three.click()
        assert section_three.is_displayed()

    def test_tabs_toogle_section_four(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toogle_accordion.click()

        section_four_iframe = self.driver.find_element_by_xpath('//*[@id="post-2654"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(section_four_iframe)
        wait_section_four = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//h3[@id="ui-id-7"]//span'
        )))

        section_four = self.driver.find_element_by_xpath('//h3[@id="ui-id-7"]//span')
        section_four.click()
        assert section_four.is_displayed()

    def test_tabs_toogle_button_toogle_icons(self):
        tabs = self.driver.find_element_by_xpath(
            '//div[@class="row price_table_holder col_4"]//a[contains(text(), "Tabs")]'
        )
        tabs.click()
        wait_tabs_toogle = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )))
        toogle_accordion = self.driver.find_element_by_xpath(
            '//div[@class="newtabs horizontal"]//li[contains(text(), "Toggle Icons")]'
        )
        toogle_accordion.click()

        button_toogle_icons_iframe = self.driver.find_element_by_xpath(
            '//*[@id="post-2654"]/div[2]/div/div/div[3]/p/iframe'
        )
        self.driver.switch_to.frame(button_toogle_icons_iframe)
        wait_button_toogle_icons = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//button[@id="toggle"]'
        )))

        button_toogle_icons = self.driver.find_element_by_xpath('//button[@id="toggle"]')
        button_toogle_icons.click()
        assert button_toogle_icons.is_displayed()

        button_toogle_icons.click()

        result_after_click_one = self.driver.find_element_by_xpath('//h3[@id="ui-id-1"]//span')
        assert result_after_click_one.is_displayed()

        result_after_click_two = self.driver.find_element_by_xpath('//h3[@id="ui-id-3"]//span')
        assert result_after_click_two.is_displayed()

        result_after_click_three = self.driver.find_element_by_xpath('//h3[@id="ui-id-5"]//span')
        assert result_after_click_three.is_displayed()

        result_after_click_four = self.driver.find_element_by_xpath('//h3[@id="ui-id-7"]//span')
        assert result_after_click_four.is_displayed()

# TOOLTIP

# есть три закладки

    def test_tooltip(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()
        assert image_based.is_displayed()
        wait_tooltip_video = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Video Based"]'
        )))
        video_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')
        video_based.click()
        assert video_based.is_displayed()
        wait_tooltip_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]'
        )))
        forms_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')
        forms_based.click()
        assert forms_based.is_displayed()

# сообщение есть и его можно закрыть
    def test_tooltip_message_image(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()
        message_image = self.driver.find_element_by_xpath(
            '//div[@rel-title="Image Based"]//div[@class="attention closable"]'
        )
        assert message_image.is_displayed()
        message_image_close = self.driver.find_element_by_xpath('//div[@rel-title="Image Based"]//a[@class="close_img"]')
        message_image_close.click()
        message_image_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_image_not.is_displayed()

    def test_tooltip_message_video(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_video = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Video Based"]'
        )))
        video_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')
        video_based.click()
        message_video = self.driver.find_element_by_xpath(
            '//div[@rel-title="Video Based"]//div[@class="attention closable"]'
        )
        assert message_video.is_displayed()
        message_video_close = self.driver.find_element_by_xpath('//div[@rel-title="Video Based"]//a[@class="close_img"]')
        message_video_close.click()
        message_video_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_video_not.is_displayed()

    def test_tooltip_message_forms(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]'
        )))
        forms_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')
        forms_based.click()
        message_forms = self.driver.find_element_by_xpath(
            '//div[@rel-title="Forms Based"]//div[@class="attention closable"]'
        )
        assert message_forms.is_displayed()
        message_forms_close = self.driver.find_element_by_xpath('//div[@rel-title="Forms Based"]//a[@class="close_img"]')
        message_forms_close.click()
        message_forms_not = self.driver.find_element_by_css_selector('#post-2679 .resp-tab-content-active > div')
        assert message_forms_not.is_displayed()

    def test_tooltip_images_vienna(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]')
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()

        image_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[1]/p[1]/iframe')
        self.driver.switch_to.frame(image_based_iframe)

        wait_tooltip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//a[contains(text(),"Vienna, Austria")]'
        )))

        vienna = self.driver.find_element_by_xpath('//a[contains(text(),"Vienna, Austria")]')
        vienna.click()
        # assert vienna.click()
        # ?????? Message: stale element reference: element is not attached to the page document

    def test_tooltip_images_london(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()

        image_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[1]/p[1]/iframe')
        self.driver.switch_to.frame(image_based_iframe)

        wait_tooltip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//a[contains(text(),"London, England")]'
        )))

        london = self.driver.find_element_by_xpath('//a[contains(text(),"London, England")]')
        london.click()

    def test_tooltip_images_link_wikimedia(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()

        image_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[1]/p[1]/iframe')
        self.driver.switch_to.frame(image_based_iframe)

        wait_tooltip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//a[contains(text(),"Wikimedia Commons")]'
        )))

        wikimedia_commons = self.driver.find_element_by_xpath('//a[contains(text(),"Wikimedia Commons")]')
        wikimedia_commons.click()
        result = self.driver.find_element_by_xpath('//*[@id="content"]')
        assert result.is_displayed()            


    def test_tooltip_images_link_cc_by(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_image = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Image Based"]'
        )))
        image_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Image Based"]')
        image_based.click()

        image_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[1]/p[1]/iframe')
        self.driver.switch_to.frame(image_based_iframe)

        wait_tooltip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//a[contains(text(),"Wikimedia Commons")]'
        )))

        cc_by = self.driver.find_element_by_xpath('//a[contains(text(),"CC BY-SA 3.0")]')
        cc_by.click()

    def test_tooltip_video(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_video = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Video Based"]'
        )))
        video_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Video Based"]')
        video_based.click()

        video_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[2]/p[1]/iframe')
        self.driver.switch_to.frame(video_based_iframe)

        wait_tooltip = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//button[@data-icon="ui-icon-circle-arrow-n"]//span[@class="ui-button-icon ui-icon ui-icon-circle-arrow-n"]'
        )))

        button_like = self.driver.find_element_by_xpath(
            '//button[@data-icon="ui-icon-circle-arrow-n"]//span[@class="ui-button-icon ui-icon ui-icon-circle-arrow-n"]'
        )
        button_like.click()
        assert button_like.is_displayed()

        button_dislike = self.driver.find_element_by_xpath('//button[@data-icon="ui-icon-circle-arrow-s"]//span')
        button_dislike.click()
        assert button_dislike.is_displayed()

        button_add_to = self.driver.find_element_by_xpath(
            '//button[@data-icon="ui-icon-circle-plus"]//span[@class="ui-button-icon ui-icon ui-icon-circle-plus"]'
        )
        button_add_to.click()
        assert button_add_to.is_displayed()

        button_open = self.driver.find_element_by_xpath(
            '//button[@class="menu ui-widget ui-button-icon-only ui-controlgroup-item ui-button ui-corner-right"]//span[@class="ui-button-icon ui-icon ui-icon-triangle-1-s"]'
        )
        button_open.click()
        button_add_to_favorites = self.driver.find_element_by_xpath(
            '//ul[@id="ui-id-1"]//li[@class="ui-menu-item"]//div[@id="ui-id-2"]'
        )
        button_add_to_favorites.click()

        button_open = self.driver.find_element_by_xpath(
            '//button[@class="menu ui-widget ui-button-icon-only ui-controlgroup-item ui-button ui-corner-right"]//span[@class="ui-button-icon ui-icon ui-icon-triangle-1-s"]'
        )
        button_open.click()
        button_add_to_funnees = self.driver.find_element_by_xpath(
            '//ul[@id="ui-id-1"]//li[@class="ui-menu-item"]//div[@id="ui-id-3"]'
        )
        button_add_to_funnees.click()

        button_open = self.driver.find_element_by_xpath(
            '//button[@class="menu ui-widget ui-button-icon-only ui-controlgroup-item ui-button ui-corner-right"]//span[@class="ui-button-icon ui-icon ui-icon-triangle-1-s"]'
        )
        button_open.click()
        button_add_to_new_playlist = self.driver.find_element_by_xpath(
            '//ul[@id="ui-id-1"]//li[@class="ui-menu-item"]//div[@id="ui-id-4"]'
        )
        button_add_to_new_playlist.click()
        # assert button_add_to_new_playlist.is_displayed()

        button_share = self.driver.find_element_by_xpath('//button[@title="Share this video"]')
        button_share.click()
        assert button_share.is_displayed()

        button_flag = self.driver.find_element_by_xpath(
            '//button[@data-icon="ui-icon-alert"]//span[@class="ui-button-icon ui-icon ui-icon-alert"]'
        )
        button_flag.click()
        assert button_flag.is_displayed()

        here_be_video = self.driver.find_element_by_xpath('//div[@class="player"]')
        assert here_be_video.is_displayed()

    def test_tooltip_forms(self):
        tooltip = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/tooltip"][text()="ToolTip"]'
        )
        tooltip.click()
        wait_tooltip_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]'
        )))
        forms_based = self.driver.find_element_by_xpath('//ul[@class="resp-tabs-list "]//li[@id="Forms Based"]')
        forms_based.click()

        forms_based_iframe = self.driver.find_element_by_xpath('//*[@id="post-2679"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(forms_based_iframe)

        wait_forms = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#lastname')))

        field_firstname = self.driver.find_element_by_css_selector('#firstname')
        field_firstname.click()
        assert field_firstname.is_displayed()

        field_lastname = self.driver.find_element_by_css_selector('#lastname')
        field_lastname.click()
        assert field_lastname.is_displayed()

        field_address = self.driver.find_element_by_css_selector('#address')
        field_address.click()
        assert field_address.is_displayed()

        button_show_help = self.driver.find_element_by_xpath('//button[contains(text(),"Show help")]')
        button_show_help.click()
        assert button_show_help.is_displayed()
        # result_name = self.driver.find_element_by_xpath('//div[@id="ui-id-12"]//div[@class="ui-tooltip-content"]')
        # result_address = self.driver.find_element_by_xpath('//button[contains(text(),"Your home or work address.")]')
        # assert result_name.is_displayed()
        # assert result_address.is_displayed()
#
# закладка alert_box кнопка try_it - работает

    def test_alert_box_simple_try_it(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@aria-labelledby="tab_item-0"]//button'
        )))
        simple_alert_box = self.driver.find_element_by_xpath('//li[@id="Simple Alert Box"]')
        simple_alert_box.click()
        try_it_simple = self.driver.find_element_by_xpath(
            '//div[@aria-labelledby="tab_item-0"]//button'
        )
        try_it_simple.click()
        assert try_it_simple.is_displayed()

    def test_alertbox_confirmation_box_try_it(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Confirmation Box"]'
        )))
        confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
        confirmation_box.click()
        try_it_confirmation = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-1"]//button')
        try_it_confirmation.click()
        assert try_it_confirmation.is_displayed()

    def test_alertbox_prompt_box_try_it(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Prompt Box"]'
        )))
        prompt_box = self.driver.find_element_by_xpath('//li[@id="Prompt Box"]')
        prompt_box.click()
        try_it_prompt_box = self.driver.find_element_by_xpath('//div[@aria-labelledby="tab_item-2"]//button')
        try_it_prompt_box.click()
        assert try_it_prompt_box.is_displayed()

# закладка alert_box убедиться что есть три закладки - работает

    def test_alert_box_simple(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@aria-labelledby="tab_item-0"]//button'
        )))
        simple_alert_box = self.driver.find_element_by_xpath('//li[@id="Simple Alert Box"]')
        simple_alert_box.click()
        assert simple_alert_box.is_displayed()

    def test_alertbox_confirmation_box(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Confirmation Box"]'
        )))
        confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
        confirmation_box.click()
        assert confirmation_box.is_displayed()

    def test_alertbox_prompt_box(self):
        alertbox = self.driver.find_element_by_xpath(
            '//div[@class="price_column "]//a[@href="https://www.globalsqa.com/demo-site/alertbox/"]'
        )
        alertbox.click()
        wait_alertbox = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Prompt Box"]'
        )))
        prompt_box = self.driver.find_element_by_xpath('//li[@id="Prompt Box"]')
        prompt_box.click()
        assert prompt_box.is_displayed()

# DIALOG_BOX
    def test_dialogbox_form(self):
        dialog_box = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/dialog-boxes/"][text()="DialogBox"]'
        )
        dialog_box.click()
        wait_form = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Form"]')))
        form = self.driver.find_element_by_xpath('//li[@id="Form"]')
        form.click()

        dialog_form_iframe = self.driver.find_element_by_xpath('//*[@id="post-2663"]/div[2]/div/div/div[1]/p[1]/iframe')
        self.driver.switch_to.frame(dialog_form_iframe)

        wait_new_user = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, 'create-user')))
        create_new_user = self.driver.find_element_by_id('create-user')
        create_new_user.click()
        assert create_new_user.is_displayed()

        input_name = self.driver.find_element_by_xpath('//input[@id="name"]')
        input_name.send_keys('lyudmila')
        input_email = self.driver.find_element_by_xpath('//input[@id="email"]')
        input_email.send_keys('lyudmilachunihina@gmail.com')
        input_password = self.driver.find_element_by_xpath('//input[@id="password"]')
        input_password.send_keys('123456789')
        button_create_account = self.driver.find_element_by_css_selector(
            'body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable.ui-resizable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)'
        )
        button_create_account.click()
        assert button_create_account.is_displayed()

    def test_dialogbox_message_box(self):
        dialog_box = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/dialog-boxes/"][text()="DialogBox"]'
        )
        dialog_box.click()
        wait_message_box = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Form"]')))
        message_box = self.driver.find_element_by_xpath('//li[@id="Message Box"]')
        message_box.click()

        dialog_message_box_iframe = self.driver.find_element_by_xpath(
            '//*[@id="post-2663"]/div[2]/div/div/div[2]/p[1]/iframe'
        )
        self.driver.switch_to.frame(dialog_message_box_iframe)

        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="ui-dialog ui-corner-all ui-widget ui-widget-content ui-front ui-dialog-buttons ui-draggable ui-resizable"]'
        )))

        window_download_complete = self.driver.find_element_by_xpath(
            '//div[@class="ui-dialog ui-corner-all ui-widget ui-widget-content ui-front ui-dialog-buttons ui-draggable ui-resizable"]'
        )
        assert window_download_complete.location

        button_ok = self.driver.find_element_by_xpath(
            '//div[@class="ui-dialog-buttonset"]//button[@class="ui-button ui-corner-all ui-widget"]'
        )
        button_ok.click()

        link_rufrum_convallis = self.driver.find_element_by_xpath('//a[@href="http://example.com"]')
        assert link_rufrum_convallis.is_displayed()

    def test_dialogbox_confirmation_box(self):
        dialog_box = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/dialog-boxes/"][text()="DialogBox"]'
        )
        dialog_box.click()
        wait_confirmation_box = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Confirmation Box"]'
        )))
        confirmation_box = self.driver.find_element_by_xpath('//li[@id="Confirmation Box"]')
        confirmation_box.click()

        dialog_confirmation_box_iframe = self.driver.find_element_by_xpath(
            '//*[@id="post-2663"]/div[2]/div/div/div[3]/p[1]/iframe'
        )
        self.driver.switch_to.frame(dialog_confirmation_box_iframe)

        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH,'//div[@role="dialog"]')))

        window_empty_recycle_bin = self.driver.find_element_by_xpath('//div[@role="dialog"]')
        assert window_empty_recycle_bin.location

        button_delete_all_items = self.driver.find_element_by_xpath(
            '//div[@class="ui-dialog-buttonset"]//button[@class="ui-button ui-corner-all ui-widget"]'
        )
        button_delete_all_items.click()

        # button_cancel = self.driver.find_element_by_css_selector(
        # 'body > div.ui-dialog.ui-corner-all.ui-widget.ui-widget-content.ui-front.ui-dialog-buttons.ui-draggable > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(2)'
        # )
        # button_cancel.click()

        link_rufrum_convallis = self.driver.find_element_by_xpath('//a[@href="http://example.com"]')
        assert link_rufrum_convallis.is_displayed()

# FRAMES

    def test_frames_open_mew_tab(self):
        frames = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/frames-and-windows/"][text()="Frames"]'
        )
        frames.click()
        wait_frames = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Open New Tab"]'
        )))

        open_new_tab = self.driver.find_element_by_xpath('//li[@id="Open New Tab"]')
        open_new_tab.click()
        assert open_new_tab.is_displayed()

        message = self.driver.find_element_by_xpath('//*[@id="post-2632"]/div[2]/div/div/div[1]/div')
        assert message.is_displayed()

        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[1]')
        button_close_message.click()

        message_close = self.driver.find_element_by_css_selector(
            '#post-2632 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > div'
        )
        assert message_close.is_displayed()

        click_here_open_tab = self.driver.find_element_by_xpath(
            '(//a[@href="#"][text()="Click Here"][text()="Click Here"])[1]'
        )
        click_here_open_tab.click()
        assert click_here_open_tab.is_displayed()

    def test_frames_open_new_window(self):
        frames = self.driver.find_element_by_xpath(
                 '//a[@href="https://www.globalsqa.com/demo-site/frames-and-windows/"][text()="Frames"]'
        )
        frames.click()
        wait_frames = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((
            By.XPATH, '//li[@id="Open New Tab"]'
        )))

        open_new_window = self.driver.find_element_by_xpath('//li[@id="Open New Window"]')
        open_new_window.click()
        assert open_new_window.is_displayed()

        message = self.driver.find_element_by_xpath(
            '(//strong[text()="Click below button to open a new window now"])[1]'
        )
        assert message.is_displayed()

        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[2]')
        button_close_message.click()

        message_close = self.driver.find_element_by_css_selector(
            '#post-2632 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > div'
        )
        assert message_close.is_displayed()

        click_here_open_tab = self.driver.find_element_by_xpath(
            '(//a[@href="#"][text()="Click Here"][text()="Click Here"])[2]'
        )
        click_here_open_tab.click()
        assert click_here_open_tab.is_displayed()

    def test_frames_iframe(self):
        frames = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/frames-and-windows/"][text()="Frames"]'
        )
        frames.click()
        wait_frames = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Open New Tab"]')))

        open_iframes = self.driver.find_element_by_xpath('//li[@id="iFrame"]')
        open_iframes.click()
        assert open_iframes.is_displayed()

        message = self.driver.find_element_by_xpath('(//div[@class="information closable"])[2]')
        assert message.is_displayed()

        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[3]')
        button_close_message.click()

        message_close = self.driver.find_element_by_css_selector(
            '#post-2632 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > div'
        )
        assert message_close.is_displayed()

# DROPDOWN

    def test_drop_down(self):
        drop_down = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/select-dropdown-menu/"][text()="DropDown"]')
        drop_down.click()
        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Select Country"]')))

        select_country = self.driver.find_element_by_xpath('//li[@id="Select Country"]')
        select_country.click()
        assert select_country.is_displayed()

        message = self.driver.find_element_by_xpath('//div[@class="information closable"]')
        assert message.is_displayed()
        button_message_close = self.driver.find_element_by_xpath('//a[@class="close_img"]')
        button_message_close.click()
        message_not = self.driver.find_element_by_css_selector('#post-2646 > div.twelve.columns > div > div > div > div')
        assert message_not.is_displayed()

        list_select_country = self.driver.find_elements_by_tag_name('option')
        assert len(list_select_country) == 249

        my_select_country = []
        for i in list_select_country:
            my_select_country.append(i)

        my_select_country[2].click()
        result = self.driver.find_element_by_xpath('//option[contains(text(), "Albania")]')
        assert result.is_displayed()

# SELECT ELEMENTS

    def test_select_elements_multiple_selection(self):
        select_elements = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/select-elements/"][text()="SelectElements"]'
        )
        select_elements.click()

        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Multiple Selection"]')))
        multiple_selection = self.driver.find_element_by_xpath('//li[@id="Multiple Selection"]')
        multiple_selection.click()
        assert multiple_selection.is_displayed()

        message = self.driver.find_element_by_xpath('(//div[@class="attention closable"])[1]')
        assert message.is_displayed()
        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[1]')
        button_close_message.click()
        message_not = self.driver.find_element_by_xpath('//div[@style="display: none;"]')
        assert message_not.location

        multiple_selection_iframe = self.driver.find_element_by_xpath(
            '//*[@id="post-2649"]/div[2]/div/div/div[1]/p/iframe'
        )
        self.driver.switch_to.frame(multiple_selection_iframe)

        item_one = self.driver.find_element_by_xpath('//li[contains(text(), "Item 1")]')
        assert item_one.location

        item_two = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 2")]')
        assert item_two.location

        item_three = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 3")]')
        assert item_three.location

        item_four = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 4")]')
        assert item_four.location

        item_five = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 5")]')
        assert item_five.location

        item_six = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 6")]')
        assert item_six.location

        item_seven = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 7")]')
        assert item_seven.location


    def test_select_elements_grid_selection(self):
        select_elements = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/select-elements/"][text()="SelectElements"]'
        )
        select_elements.click()

        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Grid Selection"]')))
        grid_selection = self.driver.find_element_by_xpath('//li[@id="Grid Selection"]')
        grid_selection.click()
        assert grid_selection.is_displayed()

        message = self.driver.find_element_by_xpath('(//div[@class="attention closable"])[2]')
        assert message.is_displayed()
        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[2]')
        button_close_message.click()
        message_not = self.driver.find_element_by_css_selector(
            '#post-2649 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > div'
        )
        assert message_not.is_displayed()

        grid_selection_iframe = self.driver.find_element_by_xpath('//*[@id="post-2649"]/div[2]/div/div/div[2]/p/iframe')
        self.driver.switch_to.frame(grid_selection_iframe)

        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//ol[@id="selectable"]/li[1]')))

        button_one = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[1]')
        button_one.click()
        assert button_one.is_displayed()

        button_two = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[2]')
        button_two.click()
        assert button_two.is_displayed()

        button_three = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[3]')
        button_three.click()
        assert button_three.is_displayed()

        button_four = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[4]')
        button_four.click()
        assert button_four.is_displayed()

        button_five = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[5]')
        button_five.click()
        assert button_five.is_displayed()

        button_six = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[6]')
        button_six.click()
        assert button_six.is_displayed()

        button_seven = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[7]')
        button_seven.click()
        assert button_seven.is_displayed()

        button_eight = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[8]')
        button_eight.click()
        assert button_eight.is_displayed()

        button_nine = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[9]')
        button_nine.click()
        assert button_nine.is_displayed()

        button_ten = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[10]')
        button_ten.click()
        assert button_ten.is_displayed()

        button_eleven = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[11]')
        button_eleven.click()
        assert button_eleven.is_displayed()

        button_twelve = self.driver.find_element_by_xpath('//ol[@id="selectable"]/li[12]')
        button_twelve.click()
        assert button_twelve.is_displayed()

    def test_select_elements_serialiaze(self):
        select_elements = self.driver.find_element_by_xpath(
            '//a[@href="https://www.globalsqa.com/demo-site/select-elements/"][text()="SelectElements"]'
        )
        select_elements.click()
        wait = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//li[@id="Serialize"]')))
        serialize = self.driver.find_element_by_xpath('//li[@id="Serialize"]')
        serialize.click()
        assert serialize.is_displayed()

        message = self.driver.find_element_by_xpath('(//div[@class="attention closable"])[3]')
        assert message.is_displayed()
        button_close_message = self.driver.find_element_by_xpath('(//a[@class="close_img"])[3]')
        button_close_message.click()
        message_not = self.driver.find_element_by_css_selector(
            '#post-2649 > div.twelve.columns > div > div > div.single_tab_div.resp-tab-content.resp-tab-content-active > div'
        )
        assert message_not.is_displayed()

        serialiaze_iframe = self.driver.find_element_by_xpath('//*[@id="post-2649"]/div[2]/div/div/div[3]/p/iframe')
        self.driver.switch_to.frame(serialiaze_iframe)
        wait_item = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.TAG_NAME, 'li')))
        item_one = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 1")]')
        item_one.click()
        assert item_one.is_displayed()

        item_two = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 2")]')
        item_two.click()
        assert item_two.is_displayed()

        item_three = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 3")]')
        item_three.click()
        assert item_three.is_displayed()

        item_four = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 4")]')
        item_four.click()
        assert item_four.is_displayed()

        item_five = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 5")]')
        item_five.click()
        assert item_five.is_displayed()

        item_six = self.driver.find_element_by_xpath('//ol[@id="selectable"]//li[contains(text(), "Item 6")]')
        item_six.click()
        assert item_six.is_displayed()


    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()
