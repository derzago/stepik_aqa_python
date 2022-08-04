from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe") # указать путь где лежит chromedriver
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//*[@id="treasure"]')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input1 = browser.find_element(by=By.XPATH, value='//*[@id="answer"]')
    input1.send_keys(y)

    input2 = browser.find_element(by=By.XPATH, value='//*[@id="robotCheckbox"]').click()
    input3 = browser.find_element(by=By.XPATH, value='//*[@id="robotsRule"]').click()
    input4 = browser.find_element(by=By.XPATH, value='/html/body/div/form/div/div/button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()