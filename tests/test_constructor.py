from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import login_page, feed_page, main_page
import conftest
import time

def test_open_constructor_by_constructor_button_by_authorized(driver):
    driver.get('https://stellarburgers.nomoreparties.site/register')

    conftest.register_user_positive(driver)

    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет")))
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, login_page.loginTitle)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    conftest.login_user(driver, conftest.email, conftest.password)

    driver.get('https://stellarburgers.nomoreparties.site/feed')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, feed_page.feedTitle)))
    driver.find_element(By.XPATH, feed_page.constructorHeaderBtn).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.processOrderBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(By.XPATH, main_page.constructorTitle).is_displayed()

def test_open_constructor_by_constructor_button_by_unauthorized(driver):
    driver.get('https://stellarburgers.nomoreparties.site/feed')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, feed_page.feedTitle)))
    driver.find_element(By.XPATH, feed_page.constructorHeaderBtn).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.loginVelvetBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(By.XPATH, main_page.constructorTitle).is_displayed()

# все что смогла тут отловить из падений - баг на стенде, когда иногда у авторизованного юзера остается кнопка входа вместо Оформить заказ
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

def test_open_constructor_by_logo_by_unauthorized(driver):
    driver.get('https://stellarburgers.nomoreparties.site/feed')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, feed_page.feedTitle)))
    driver.find_element(By.CSS_SELECTOR, feed_page.logoCSS).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.loginVelvetBtn)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' and driver.find_element(By.XPATH, main_page.constructorTitle).is_displayed()

def test_select_tabs_on_constructor_page(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.loginVelvetBtn)))

    # переключение на таб Начинки
    driver.find_element(By.XPATH, main_page.tabToppings).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.selectedToppings)))

    # переключение на таб Соусы
    driver.find_element(By.XPATH, main_page.tabSauces).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.selectedSauces)))

    # переключение на таб Булки
    # c WebDriverWait для кликабельности таба тоже теперь упало, перепробовала несколько вариантов - завелся так, до этого перед отправкой раз 5 прогоняла - стабильно проходил))
    time.sleep(1)
    driver.find_element(By.XPATH, main_page.tabBreads).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.selectedBreads)))