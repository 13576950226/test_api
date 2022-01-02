from selenium.webdriver.common.by import By


class LoginPageElement:
    go_login_element = (By.XPATH, "//a[@href='//login.51job.com/login.php']")
    username_element = (By.XPATH, "//input[@id='loginname']")
    password_element = (By.XPATH, "//input[@id='password']")
    login_button_element = (By.XPATH, "//button[@id='login_btn']")
    drag_and_drop_element = (By.XPATH, "//p[@id='slide_btn']")