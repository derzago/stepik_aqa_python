from selenium import webdriver
import math
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe")  # указать путь где лежит chromedriver
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

input1 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()

new_window = browser.window_handles[1] # Выбираем вторую вкладку
browser.switch_to.window(new_window) # Переключаемся на неё

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(by=By.XPATH, value='//*[@id="input_value"]').text
y = calc(x)

input2 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input2.send_keys(y)

input3 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()