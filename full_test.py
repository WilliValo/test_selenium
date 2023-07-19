from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Safari()
driver.maximize_window()
driver.get("https://qa-mesto.praktikum-services.ru/")


driver.find_element(By.ID, "email").send_keys("some_email")
driver.find_element(By.ID, "password").send_keys("some_password")
driver.find_element(By.CLASS_NAME, "auth-form__button").click()

WebDriverWait(driver, 30).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))

old_avatar_url = "https://pictures.s3.yandex.net/resources/jacques-cousteau_1604399756.png"

driver.find_element(By.CLASS_NAME, "profile__image").click()

avatar_url = "https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png"
driver.find_element(By.ID, "owner-avatar").send_keys(avatar_url)

driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']").click()

driver.refresh()

WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))

style = driver.find_element(By.CLASS_NAME, "profile__image").get_attribute("style")

assert avatar_url in style


driver.find_element(By.CLASS_NAME, "profile__image").click()


driver.find_element(By.ID, "owner-avatar").send_keys(old_avatar_url)


driver.find_element(By.XPATH, ".//form[@name='edit-avatar']/button[text()='Сохранить']").click()


driver.refresh()


WebDriverWait(driver, 30).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "profile__description")))


style = driver.find_element(By.CLASS_NAME, "profile__image").get_attribute("style")

assert old_avatar_url in style

