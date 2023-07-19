from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Safari()
driver.get('https://qa-mesto.praktikum-services.ru/signin')

driver.find_element(By.ID, "email").send_keys("co-pilot29@yandex.ru")
driver.find_element(By.ID, "password").send_keys("123321")

driver.find_element(By.CLASS_NAME, "auth-form__button").click()

WebDriverWait(driver, 10)



