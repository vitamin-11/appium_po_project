import allure
import pytest
from pages.drag_page import DragPage
from pages.login_page import LoginPage
from pages.forms_page import FormsPage
from pages.swipe_page import SwipePage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.epic("移动端自动化")
@allure.feature("核心业务流程")
@allure.story("端到端全流程")
@allure.title("登录 → 填表 → 滑动 → 拖拽完整业务流")
@allure.description("覆盖 Native Demo App 的四个核心页面操作，验证端到端流程可用")
@allure.severity(allure.severity_level.CRITICAL)
def test_full_flow(driver):

    with allure.step("登录模块：进入登录页并完成登录"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Login").click()
        LoginPage(driver).login("demo", "password")
        # assert LoginPage(driver).is_login_success() == True

    with allure.step("表单模块：进入表单页，填写输入框并切换开关"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Forms").click()
        forms = FormsPage(driver)
        forms.fill_input("自动化测试").toggle_switch()

    with allure.step("滑动模块：进入滑动页，左滑删除条目"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        swipe = SwipePage(driver)
        swipe.swipe_left()
        # assert swipe.is_item_visible("已删除项") == False

    with allure.step("拖拽模块：进入拖拽页，完成拼图拖拽"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag").click()
        drag = DragPage(driver)
        drag.solve_puzzle()