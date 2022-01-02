import logging
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base


class Way(Base):

    def fand_element(self, location):  # 定位元素
        try:
           element = WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element(location[0], location[1]))
        except:
            logging.INFO("定位异常")
        return element

    def click(self, location):  # 点击
        self.fand_element(location).click()

    def input(self, location, value):  # 输入
        self.fand_element(location).send_keys(value)
