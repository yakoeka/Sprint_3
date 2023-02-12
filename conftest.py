import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages import registration_page, login_page

name = 'tester'
email = f'kataiakovleva6{random.randint(10, 99)}@ya.ru'
password = 'qwerty9ytrewq'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def register_user_positive(driver):
    driver.find_element(By.XPATH, registration_page.fieldName).send_keys(name)
    driver.find_element(By.XPATH, registration_page.fieldEmail).send_keys(email)
    driver.find_element(By.XPATH, registration_page.fieldPassword).send_keys(password)
    driver.find_element(By.XPATH, registration_page.signUpBtn).click()

def login_user(driver, email,password):
    driver.find_element(By.XPATH, login_page.fieldEmail).send_keys(email)
    driver.find_element(By.XPATH, login_page.fieldPassword).send_keys(password)
    driver.find_element(By.XPATH, login_page.loginBtn).click()
