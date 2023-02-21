from selenium.webdriver.common.by import By
import pytest
from settings import valid_phone, valid_email, valid_login, valid_password


def test_login_email(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()


def test_login_login(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()


def test_login_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Вводим password
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    # Нажимаем на кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что мы зашли в личный кабинет
    assert pytest.driver.find_element(By.XPATH, '//h3[text()="Учетные данные"]')
    # Выходим из учетной записи
    pytest.driver.find_element(By.ID, 'logout-btn').click()
