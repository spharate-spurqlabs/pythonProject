from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("Users is on calculator page")
def step_impl(context):
    context.driver = webdriver.Chrome("Resource/chromedriver.exe")
    context.driver.get("https://www.calculator.net/")
    context.driver.maximize_window()


@when("Users clicks on (?P<num1>.+) number")
def step_impl(context, num1):
    num1 = context.table[0][0]
    print("Num1 is", +num1)
    for i in range(0, len(num1)):
        context.driver.find_element("xpath", " //span[text()='" + num1[i] + "']").click()
        sleep(2)

    # operator = context.table[0][2]
    # context.driver.find_element("xpath", " //span[text()='" + operator + "']").click()
    # sleep(2)
    #
    # num2 = context.table[0][1]
    # print("num2 is :" + num2)
    # sleep(2)


@step("Users clicks on (?P<operator>.+) operator")
def step_impl(context, operator):
    additionalOperator = context.driver.find_element("xpath", " //span[text()='" + operator + "']")
    additionalOperator.click()
    sleep(2)


@step("Users clicks in (?P<num2>.+) number")
def step_impl(context, num2):
    num2 = context.driver.find_element("xpath", "//span[text()='6']")
    num2.click()
    sleep(2)


# @when("Users clicks on 9 number")
# def step_impl(context):
#   num1 = context.driver.find_element("xpath", "//span[text()='9']")
#   num1.click()
#   sleep(2)

# @when("Users clicks on 9 number")
# def step_impl(context, number):
#     context.calculatorPage.click_number(number)
#
#
# @step("Users clicks on \+ operator")
# def step_impl(context, operator):
#     context.calculatorPage.click_operator(operator)
#
#
# @step("Users clicks in 6 number")
# def step_impl(context, number):
#     num2 = context.driver.find_element("xpath", "//span[text()='6']")
#     num2.click()
#
#
# sleep(2)
#
#
# @then("Users verify the result 15")
# def step_impl(context, total):
#     result = context.calculatorPage.verify_result()
#     assert result == total
#

@then("Users verify the result Total(?P<total>.+)")
def step_impl(context, total):
    result = context.driver.find_element(By.ID, "sciOutPut").text
    result = result.lstrip()
    print("Result is:" + result)
    assert result == total
    sleep(3)


@when("User enter following values")
def step_impl(context):
    for row in context.table:
        num1 = row[0][0]
        num2 = row[1][0]
        operator = row[2][0]
        context.driver.find_element("xpath", "//span[text()='" + num1 + "']").click()
        sleep(2)
        context.driver.find_element("xpath", "//span[text()='" + operator + "']").click()
        sleep(2)
        context.driver.find_element("xpath", "//span[text()='" + num2 + "']").click()
        sleep(2)
