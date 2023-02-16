from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import login_page, profile_page

import conftest


def test_open_profile_by_button_in_header(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    conftest.register_user_positive(driver)

    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_page.loginTitle)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    conftest.login_user(driver, conftest.email, conftest.password)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, 'Личный Кабинет')))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, profile_page.logOutBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'