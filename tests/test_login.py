import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.login_page import LoginPage


@allure.epic("移动端自动化")
@allure.feature("登录模块")
@allure.story("用户登录")
@allure.title("验证正常账号密码登录成功")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(driver):

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()

    with allure.step("输入账号密码并登录"):
        page = LoginPage(driver)
        page.login("demo", "password")
    with allure.step("验证登录状态"):
        assert page.is_logged_in()