from selenium.webdriver.common.by import By
import pytest
from settings import valid_phone, valid_email, valid_login, valid_ls


def test_change_tab_phone(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим номер телефона
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_phone)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на таб по номеру телефона
    assert pytest.driver.find_element(By.XPATH, "//*[@class='rt-tab rt-tab--small rt-tab--active' and "
                                                "@id='t-btn-tab-phone']")


def test_change_tab_email(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим email
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_email)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на таб по Почта
    assert pytest.driver.find_element(By.XPATH, "//*[@class='rt-tab rt-tab--small rt-tab--active' and "
                                                "@id='t-btn-tab-mail']")


def test_change_tab_login(open_login_page):

    # Нажимаем кнопку Телефон
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    pytest.driver.implicitly_wait(10)
    # Вводим Логин
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_login)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на авторизацию по логину
    assert pytest.driver.find_element(By.XPATH, "//*[@class='rt-tab rt-tab--small rt-tab--active' and "
                                                "@id='t-btn-tab-login']")


def test_change_tab_ls(open_login_page):

    # Нажимаем кнопку Почта
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    pytest.driver.implicitly_wait(10)
    # Вводим валидный лицевой счет
    pytest.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(valid_ls)
    # Нажимаем на поле Пароль
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').click()
    # Проверяем, что таб переключился на таб по Лицевому счету
    assert pytest.driver.find_element(By.XPATH, "//*[@class='rt-tab rt-tab--small rt-tab--active' and "
                                                "@id='t-btn-tab-ls']")
