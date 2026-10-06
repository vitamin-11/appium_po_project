from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SettingsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_apps(self):
        """点击设置首页的 Apps 菜单项"""
        apps_item = self.wait.until(
            EC.element_to_be_clickable((
                AppiumBy.XPATH,
                "//android.widget.RelativeLayout[@resource-id='com.android.settings:id/text_frame']"
                "[.//android.widget.TextView[@text='Apps']]"
            ))
        )
        apps_item.click()
        return self

    def get_page_title(self):
        """获取当前页面的标题文字"""
        title = self.wait.until(
            EC.presence_of_element_located((
                AppiumBy.XPATH,
                "//android.widget.TextView[@resource-id='android:id/title']"
            ))
        )
        return title.text