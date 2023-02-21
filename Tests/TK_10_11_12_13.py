from selenium.webdriver.common.by import By
import pytest


def test_empty_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите номер телефона"]')


def test_empty_email(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите адрес, указанный при регистрации"]')


def test_empty_login(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите логин, указанный при регистрации"]')


def test_empty_ls(open_login_page):

    # Нажимаем кнопку Логин
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Нажимаем кнопку Войти
    pytest.driver.find_element(By.ID, 'kc-login').click()
    # Проверяем, что появилась подсказка об ошибке ввода
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Введите номер вашего лицевого счета"]')
