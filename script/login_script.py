import allure
from pytest_allure_dsl import allure
from config.config import logging
from selenium.webdriver import ActionChains
from base.way import Way
from script.location_element.login_page_element import LoginPageElement


class Login_script(Way, LoginPageElement):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    @allure.step("点击已有账号去登录")
    def go_login_button(self):  # 点击已有账号去登录
        self.click(self.go_login_element)

    @allure.step("输入用户名")
    def input_username(self, username):  # 输入用户名
        allure.attach("输入用户名:%s" % username, "")
        self.input(self.username_element, username)

    @allure.step("输入密码")
    def input_password(self, password):  # 输入密码
        allure.attach("输入密码%s" % password, "")
        self.input(self.password_element, password)

    @allure.step("点击登录按钮")
    def click_login_button(self):  # 点击登录按钮
        self.click(self.login_button_element)

    @allure.step("拖动验证条")
    def drag_and_drop(self):
        element = self.fand_element(self.drag_and_drop_element)
        ActionChains(self.driver).drag_and_drop_by_offset(element, 380, 0).perform()

    @allure.step("是否登录成功")
    def assert_login(self):
        try:
            assert self.fand_element(self.login_button_element).text == "登录"
            print("登录成功")
        except AssertionError:
            raise logging.info("登录失败")

    @allure.step("登录")
    def login_way(self, username, password):
        handle = self.driver.current_window_handle
        self.go_login_button()
        handles = self.driver.window_handles
        for i in handles:
            if i != handle:
                self.driver.switch_to_window(i)
        self.input_username(username)
        logging.info("输入用户名:%s" % username)
        self.input_password(password)
        logging.info("输入密码:%s" % password)
        # self.drag_and_drop()
        self.click_login_button()
        logging.info("点击登录")
        self.assert_login()