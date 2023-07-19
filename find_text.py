from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Safari()

driver.get('https://qa-mesto.praktikum-services.ru/signin')

assert driver.find_element(By.CLASS_NAME, "auth-form__title").text == 'Вход'