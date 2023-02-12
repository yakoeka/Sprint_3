from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import login_page, main_page

import conftest

def test_login_by_header_button(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    conftest.register_user_positive(driver)

    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_page.loginTitle)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    conftest.login_user(driver, conftest.email, conftest.password)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.processOrderBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'