from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DragPage:
    def __init__(self, driver):
        self.driver = driver

    def solve_puzzle(self):
        wait = WebDriverWait(self.driver, 10)
        source = wait.until(EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "drag-c1")))
        target = wait.until(EC.presence_of_element_located(
            (AppiumBy.ACCESSIBILITY_ID, "drop-c1")))
        self.driver.drag_and_drop(source, target)
        return self