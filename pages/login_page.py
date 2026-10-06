from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login(self,username,password):
        # 进入登录页
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()

        #输入账户密码
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "input-email"))
        ).send_keys(username)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "input-password").send_keys(password)
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "button-LOGIN").click()
        return self

    def is_logged_in(self):
        self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,"Forms"))
        )
        return True