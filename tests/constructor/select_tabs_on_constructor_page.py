from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages import main_page

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
    # ожидание добавила только в этом тесте, тк почему-то именно на нем падал, потому что не мог нажать на этот таб
    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, main_page.tabBreads)))
    driver.find_element(By.XPATH, main_page.tabBreads).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, main_page.selectedBreads)))