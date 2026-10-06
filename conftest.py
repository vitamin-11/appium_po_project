import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def driver():
    if os.getenv("USE_CLOUD") == "1":
        #连接 BrowserStack 的Appium hub
        print("=== 创建 driver 成功 ===")
        print("=== 测试结束，准备quit ===")
    else:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.device_name = "Android Emulator"
        options.no_reset = True
        options.load_capabilities({
            "appium:appPackage": "com.wdiodemoapp",
            "appium:appActivity": ".MainActivity"
        })
        # options.load_capabilities({
        #     "appium:appPackage": "com.android.settings",
        #     "appium:appActivity": ".Settings"
        # })

        d = webdriver.Remote("http://127.0.0.1:4723", options=options)
        print("=== 创建 driver 成功 ===")
        yield d
        print("=== 测试结束，准备quit ===")
        d.quit()

import allure

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="失败截图",
                attachment_type=allure.attachment_type.PNG
            )