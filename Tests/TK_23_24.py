import time
import pytest
from selenium.webdriver.common.by import By
from settings import valid_phone, fake_firstname, fake_lastname, valid_password


def test_registration_with_used_phone_redirect_auth(open_login_page):
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')

    # Вводим Имя
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(fake_firstname)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(fake_lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_phone)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Нажимаем на кнопку 'Войти'
    pytest.driver.find_element(By.XPATH, '//button[text()="Войти"]').click()
    # Проверяем, что перешли на страницу авторизации
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Авторизация"]')


def test_registration_with_used_phone_check_code():
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')

    # Вводим Имя
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(fake_firstname)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(fake_lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_phone)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Нажимаем на ссылка 'Зарегистрироваться'
    pytest.driver.find_element(By.XPATH, '//button[text()="Зарегистрироваться"]').click()
    # Проверяем, что перешли на страницу для ввода кода подтверждения
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение телефона"]')
    time.sleep(5)
