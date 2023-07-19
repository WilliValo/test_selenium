from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Safari()
driver.maximize_window()

driver.get(' https://qa-mesto.praktikum-services.ru/')
assert '/signin' in driver.current_url