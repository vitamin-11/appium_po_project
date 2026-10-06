import allure
from pages.drag_page import DragPage
from pages.swipe_page import SwipePage
from appium.webdriver.common.appiumby import AppiumBy


@allure.epic("移动端自动化")
@allure.feature("手势操作")
@allure.story("滑动与拖拽")
@allure.title("滑动与拖拽组合验证")
@allure.severity(allure.severity_level.NORMAL)
def test_swipe_and_drag(driver):

    with allure.step("进入滑动页面并执行左滑"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Swipe").click()
        SwipePage(driver).swipe_left()

    with allure.step("切换到底部导航栏 Drag 页面"):
        driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Drag").click()

    with allure.step("执行拖拽拼图验证"):
        DragPage(driver).solve_puzzle()