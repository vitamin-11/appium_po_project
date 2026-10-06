from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwipePage:
    def __init__(self, driver):
        self.driver = driver

    def swipe_left(self):
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        y = size['height'] * 0.5
        self.driver.swipe(start_x, y, end_x, y, duration=500)
        return self