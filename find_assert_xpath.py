from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Safari()
driver.maximize_window()

driver.get("https://qa-mesto.praktikum-services.ru/")

driver.find_element(By.CLASS_NAME, "auth-form__title")

elements = driver.find_elements(By.XPATH, ".//img")

assert len(elements) > 2