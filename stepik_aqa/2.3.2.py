from selenium import webdriver
import math
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe")  # указать путь где лежит chromedriver
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

input3 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
y = calc(x)

input1 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input1.send_keys(y)

input2 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()