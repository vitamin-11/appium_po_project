from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. 配置 Capabilities
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "Android Emulator"  # 模拟器用这个；真机可填手机型号或忽略
# options.app_package = "com.android.settings"
# options.app_activity = ".Settings"
options.no_reset = True  # 不清除 App 数据

options.load_capabilities({
    "appium:appPackage": "com.android.settings",
    "appium:appActivity": ".Settings"
})

# 2. 连接 Appium Server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 15)

try:
    #等待设置界面加载完成
    wait.until(lambda d: "com.android.settings" in d.current_package)

    # 3. 定位并点击 “Apps” 菜单项
    apps_item = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            "//android.widget.RelativeLayout[@resource-id='com.android.settings:id/text_frame']"
            "[.//android.widget.TextView[@text='Apps']]"
        ))
    )
    apps_item.click()
    print("成功点击 Apps")

finally:
    driver.quit()
    print("会话已结束")