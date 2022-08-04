from selenium import webdriver
import math
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe")  # указать путь где лежит chromedriver
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)
browser.execute_script("return arguments[0].scrollIntoView(true);", input1)


input2 = browser.find_element(by=By.XPATH, value='//*[@id="robotCheckbox"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
input2.click()

input3 = browser.find_element(by=By.XPATH, value='//*[@id="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
input3.click()

input4 = browser.find_element(by=By.XPATH, value='/html/body/div/form/button')
browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
input4.click()