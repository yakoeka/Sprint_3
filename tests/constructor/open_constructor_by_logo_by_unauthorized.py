from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import feed_page, main_page

def test_open_constructor_by_logo_by_unauthorized(driver):
    driver.get('https://stellarburgers.nomoreparties.site/feed')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, feed_page.feedTitle)))
    driver.find_element(By.CSS_SELECTOR, feed_page.logoCSS).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.loginVelvetBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(By.XPATH, main_page.constructorTitle).is_displayed()