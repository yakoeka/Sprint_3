import random

from selenium.webdriver.common.by import By
from pages import registration_page

def test_register_user_with_invalid_password(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    name = 'tester'
    email = f'kataiakovleva6{random.randint(10, 99)}@ya.ru'
    # пароль меньше 6 символов
    password = 'qwert'
    driver.find_element(By.XPATH, registration_page.fieldName).send_keys(name)
    driver.find_element(By.XPATH, registration_page.fieldEmail).send_keys(email)
    driver.find_element(By.XPATH, registration_page.fieldPassword).send_keys(password)

    driver.find_element(By.XPATH, registration_page.signUpBtn).click()

    error_text = driver.find_element(By.XPATH, registration_page.errorTextForInvalidPassword)
    assert error_text.is_displayed() and error_text.text == 'Некорректный пароль'
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'