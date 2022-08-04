from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome(
    r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe")  # указать путь где лежит chromedriver
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, 'book').click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x = browser.find_element(by=By.XPATH, value='//*[@id="input_value"]').text
y = calc(x)

input2 = browser.find_element(By.XPATH, '//*[@id="answer"]')
input2.send_keys(y)

input3 = browser.find_element(By.XPATH, '/html/body/form/div/div/button').click()