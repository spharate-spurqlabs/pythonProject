from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("We are on calculator page")
def step_impl(context):
    context.driver = webdriver.Chrome("Resource/chromedriver.exe")
    context.driver.get("https://www.calculator.net/bmi-calculator.html?ctype=metric")
    context.driver.maximize_window()


@when("User click on 24 field")
def step_impl(context):
    age = context.driver.find_element(By.ID, 'cage')
    age.clear()
    age.send_keys(24)
    age.click()
    sleep(2)


@when("User click on female field")
def step_impl(context):
    try:

        gender_list = context.driver.find_element(By.ID,'calinputtable')
        print('GenderList', len(gender_list))
        for gen in gender_list:
            print('Gender', gen.get_attribute('value'), gen)
            if gen.get_attribute('value') == 'm':
                gen.click()
                sleep(2)
                break
    except:
        pass


@when("User click on 180 field")
def step_impl(context):
    height = context.driver.find_element(By.ID, 'cheightmeter')
    height.clear()
    height.send_keys(180)
    height.click()
    sleep(2)


@when("User click on 60 field")
def step_impl(context):
    weight = context.driver.find_element(By.ID, 'ckg')
    weight.clear()
    weight.send_keys(45)
    weight.click()
    sleep(2)


@then("We can Calculate BMI")
def step_impl(context):
    calculate = context.driver.find_element("xpath", "//input[@value='Calculate']")
    calculate.click()
    sleep(2)
