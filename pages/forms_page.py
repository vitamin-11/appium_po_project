from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TouchAction:
    pass


class FormsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def fill_input(self, text):
        """在输入框中填写文本"""
        input_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "text-input"))
        )
        input_field.clear()
        input_field.send_keys(text)
        return self

    def get_input_text(self):
        """获取输入框中当前的文本"""
        input_field = self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "input-text-result"))
        )
        return input_field.text

    def toggle_switch(self):
        """点击开关控件"""
        switch = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.Switch[@content-desc='switch']"
            ))
        )
        # switch = self.wait.until(
        #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "switch"))
        # )
        switch.click()
        return self

    def is_switch_on(self):
        switch = self.wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.Switch[@content-desc='switch']"
            ))
        )
        value = switch.get_attribute("checked")
        # 兼容 "true" / True / "1" 等多种返回格式
        return str(value).lower() in ("true", "1")

    # def is_switch_on(self):
    #     """判断开关是否处于打开状态"""
    #     switch = self.wait.until(
    #         EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "switch-text"))
    #     )
    #     return switch.get_attribute("checked") == "true"

    def select_dropdown_option(self, option_text):
        # 点击下拉框容器
        dropdown = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//*[@resource-id='android_touchable_wrapper']"
            ))
        )
        dropdown.click()

        # 等选项列表弹出，选择目标选项
        option = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                f"//*[@text='{option_text}']"
            ))
        )
        option.click()
        return self

    def get_selected_dropdown_text(self):
        # 选中后文字会写进 resource-id="text_input" 的 EditText
        dropdown_text = self.wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//*[@resource-id='text_input']"
            ))
        )
        return dropdown_text.text

    # def select_dropdown_option(self, option_text):
    #     """点击下拉框并选择指定选项"""
    #     dropdown = self.wait.until(
    #         EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Dropdown"))
    #     )
    #     dropdown.click()
    #
    #     option = self.wait.until(
    #         EC.element_to_be_clickable((
    #             AppiumBy.XPATH,
    #             f"//*[@text='{option_text}']"
    #         ))
    #     )
    #     option.click()
    #     return self
    #
    # def get_selected_dropdown_text(self):
    #     """获取下拉框当前选中的文本"""
    #     dropdown_text = self.wait.until(
    #         EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "text_input"))
    #     )
    #     return dropdown_text.text

    def click_active_button(self):
        """点击 Active 按钮，触发弹窗"""
        self.wait.until(
            EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "button-Active"))
        ).click()
        return self

    def confirm_popup(self):
        """确认弹窗（点击弹窗中的 OK 按钮）"""
        self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//*[@text='OK' or @text='确定']"
            ))
        ).click()
        return self