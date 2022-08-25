from time import sleep

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CalculatorPage:
    def __init__(self, context):
        self.context = context
        self.num1 = "//span[text()='1']"
        self.num2 = "//span[text()='2']"
        self.num3 = "//span[text()='3']"
        self.num4 = "//span[text()='4']"
        self.addition = "//span[text()='+']"

    def click_number(self, number):
        self.driver.find_element("xpath", "//span[text()='" + number + "']").click()
        sleep(2)

    def click_operator(self, operator):
        self.driver.find_element("xpath", "//span[text()='" + operator + "']").click()
        sleep(2)

    def verify_result(self):
        result = self.driver.find_element(By.ID, "sciOutPut").text
        result = result.lstrip()
        return result
