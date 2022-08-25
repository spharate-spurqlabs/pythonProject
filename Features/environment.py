from selenium import webdriver
from Pages.BasePage import BasePage
from Pages.CaculatorPage import CalculatorPage


def before_all(context):
    context.driver = webdriver.Chrome("Resource/chromedriver.exe")
    context.driver.get("https://www.calculator.net/")
    context.driver.maximize_window()
    base_page = BasePage(context.driver)
    context.calculatorPage = CalculatorPage(base_page)


def after_all(context):
    context.driver.close()
