from selenium.webdriver.common.by import By
import pytest
from settings import long_phone, short_phone


def test_long_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(long_phone)
    # Проверяем, что в поле только разрешенное количество символов
    assert pytest.driver.find_element(By.XPATH, '//input[@value="79817258900"]')


def test_short_phone(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(short_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что появилась подсказка Неверный формат телефона
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Неверный формат телефона"]')