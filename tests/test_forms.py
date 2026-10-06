import allure
from appium.webdriver.common.appiumby import AppiumBy

from pages.forms_page import FormsPage


@allure.epic("移动端自动化")
@allure.feature("表单操作")
@allure.story("输入框填写")
@allure.title("验证输入框填写与文本获取")
@allure.severity(allure.severity_level.NORMAL)
def test_fill_input(driver):

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Forms").click()

    with allure.step("填写输入框并验证内容"):
        forms = FormsPage(driver)
        forms.fill_input("自动化测试")
        assert forms.get_input_text() == "自动化测试"


@allure.epic("移动端自动化")
@allure.feature("表单操作")
@allure.story("开关切换")
@allure.title("验证开关切换状态反转")
@allure.severity(allure.severity_level.NORMAL)
def test_toggle_switch(driver):
    with allure.step("记录初始状态，切换开关并验证状态反转"):
        forms = FormsPage(driver)
        initial = forms.is_switch_on()
        forms.toggle_switch()
        assert forms.is_switch_on() != initial


@allure.epic("移动端自动化")
@allure.feature("表单操作")
@allure.story("下拉框选择")
@allure.title("验证下拉框选项选择")
@allure.severity(allure.severity_level.NORMAL)
def test_select_dropdown(driver):
    with allure.step("选择下拉框选项并验证选中内容"):
        forms = FormsPage(driver)
        forms.select_dropdown_option("Appium is awesome")
        assert "Appium is awesome" in forms.get_selected_dropdown_text()