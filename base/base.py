import unittest
from selenium import webdriver


class Base(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://mkt.51job.com/tg/sem/pz_v2.html?from=baidupz")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
