from selenium.webdriver.common.by import By


class HomePageElement:
    home_page_element = (By.XPATH, "//a[@href='//www.51job.com/']")
    work_position_element = (By.XPATH, "//input[@id='work_position_input']")
    yz_element = (By.XPATH, "//li[@id='work_position_click_center_left_each_102000']")
    yaan_element = (By.XPATH, "//em[@id='work_position_click_center_right_list_category_102000_091800']")
    confirm_element = (By.XPATH, "//span[@id='work_position_click_bottom_save']")