import pytest_allure_dsl
from logz import log
from base.way import Way
from script.location_element.home_page_element_loaction import HomePageElement


class Homepage(Way, HomePageElement):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def click_home_page(self):  # 1
        self.click(self.home_page_element)

    def click_work_position(self):  # 2
        self.click(self.work_position_element)

    def click_yz(self):
        self.click(self.yz_element)

    def click_zhu_hai(self):
        self.click(self.yaan_element)

    def click_confirm(self):
        self.click(self.confirm_element)

    def scroll_y(self):
        js = "window.scrollTo(0,5000)"
        self.driver.execute_script(js)

    def location_zhu_hai(self):
        log.info("点击首页")
        self.click_home_page()
        log.info("选择地区")
        self.click_work_position()
        log.info("点击yz")
        self.click_yz()
        log.info("点击珠海")
        self.click_zhu_hai()
        log.info("点击确定")
        self.click_confirm()
        log.info("拖动滚动条")
        self.scroll_y()
