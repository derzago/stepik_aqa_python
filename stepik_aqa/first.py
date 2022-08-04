from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://test2efis.eosan.ru/efis/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

    loginbox = browser.find_element(by=By.XPATH,
                                   value='/html/body/div/div/div/form/div[1]/input')  # найти поле ввода логина
    loginbox.clear() # Очистить поле
    loginbox.send_keys('--admin@efis')  # Ввести логин

    passwordbox = browser.find_element(by=By.XPATH,
                                      value='/html/body/div/div/div/form/div[2]/input')  # найти поле ввода пароля
    loginbox.clear() # Очистить поле
    passwordbox.send_keys('--admin@efis')  # ввести пароль

    login_button = browser.find_element(by=By.XPATH, value='/html/body/div/div/div/form/button[1]').click()  # найти и нажать кнопку "Войти"

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()