from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome(r"C:\projects\ui_tests\tests\helpers\webdriver\chromedriver.exe") # указать путь где лежит chromedriver
    browser.get(link)

    number1 = browser.find_element(by=By.XPATH, value='//*[@id="num1"]').text
    number2 = browser.find_element(by=By.XPATH, value='//*[@id="num2"]').text

    x = int(number1) + int(number2)
    print(x)

    input1 = browser.find_element(by=By.XPATH, value='//*[@id="dropdown"]').click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(f'{x}') # ищем элемент с текстом "Python"

    number3 = browser.find_element(by=By.XPATH, value='/html/body/div/form/button').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()