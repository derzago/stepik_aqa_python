from selenium import webdriver
import math
from selenium.webdriver.common.by import By

browser = webdriver.Chrome(
    r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe")  # указать путь где лежит chromedriver
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[1]').send_keys('Alexxx')
input2 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[2]').send_keys('Wot')
input3 = browser.find_element(By.XPATH, '/html/body/div/form/div/input[3]').send_keys('AlWo@bk.ru')

directory = r"C:\Users\tolstovas\Desktop\aaa.txt"
input4 = browser.find_element(By.XPATH, '//*[@id="file"]').send_keys(r"C:\Users\tolstovas\Desktop\aaa.txt")

input5 = browser.find_element(By.XPATH, '/html/body/div/form/button').click()