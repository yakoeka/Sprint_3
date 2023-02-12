from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import login_page, feed_page, main_page

import conftest

def test_open_constructor_by_logo_by_authorized(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    conftest.register_user_positive(driver)

    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_page.loginTitle)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    conftest.login_user(driver, conftest.email, conftest.password)

    driver.get('https://stellarburgers.nomoreparties.site/feed')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, feed_page.feedTitle)))
    driver.find_element(By.CSS_SELECTOR, feed_page.logoCSS).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.processOrderBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(By.XPATH, main_page.constructorTitle).is_displayed()