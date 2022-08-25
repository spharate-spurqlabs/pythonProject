from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("Resource/chromedriver.exe")
driver.get("https://www.calculator.net/")
driver.maximize_window()

title = driver.title
print("this is the title name:"+title)

assert title == "Calculator.net: Free Online Calculators - Math, Fitness, Finance, Science"

num1 = driver.find_element("xpath", "//span[text()='9']")
num1.click()
sleep(2)

additionalOperator = driver.find_element("xpath", " //span[text()='+']")
additionalOperator.click()
sleep(2)

num2 = driver.find_element("xpath", "//span[text()='6']")
num2.click()
sleep(2)

result = driver.find_element(By.ID, "sciOutPut").text
result = result.lstrip()
print("Result is:"+result)
assert result == "13"
driver.close()

