# https://github.com/RubanQA/Test-automation/tree/main/stepik_test_automation_course
# https://github.com/AlexVokhmin/Stepik_PyTest
# https://github.com/VashkevichO/stepik_auto_tests_course/tree/master

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
#link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

nameInput = browser.find_element(By.CSS_SELECTOR, ".first_class [placeholder='Input your first name']")
nameInput.send_keys("Alexxx")

lastnameInput = browser.find_element(By.CSS_SELECTOR, ".second_class [placeholder='Input your last name']")
lastnameInput.send_keys("Wots")

emailInput = browser.find_element(By.CSS_SELECTOR, ".third_class [placeholder='Input your email']")
emailInput.send_keys("AlWo@bk.com")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(1)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

assert "Congratulations! You have successfully registered!" == welcome_text
browser.close()