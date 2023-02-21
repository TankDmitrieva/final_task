import time
import pytest
from selenium.webdriver.common.by import By
from settings import fake_firstname, valid_password, fake_lastname, not_valid_password, fake_password, \
    not_valid_firstname, fake_email


def test_invalid_password_for_registration(open_login_page):

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
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(fake_email)
    pytest.driver.implicitly_wait(3)
    # Вводим невалидный пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(not_valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').click()
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Проверяем наличие ошибок при вводе неправильного пароля
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[text()= "Пароль должен содержать хотя бы 1 спецсимвол или '
                                      'хотя бы одну цифру"]')
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[text()= "Длина пароля должна быть не менее 8 символов"]')
    time.sleep(10)


def test_invalid_password_confirm_for_registration(open_login_page):

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
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(fake_email)
    pytest.driver.implicitly_wait(3)
    # Вводим невалидный пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(fake_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    time.sleep(5)
    # Проверяем, что под полем "Подтверждение пароля" об ошибке:
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Пароли не совпадают"]')


def test_invalid_name_for_registration(open_login_page):

    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')

    # Вводим невалидное Имя
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(not_valid_firstname)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(fake_lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(fake_email)
    pytest.driver.implicitly_wait(3)
    # Вводим невалидный пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    time.sleep(5)
    # Проверяем, что под полем "Имя" появляется сообщение об ошибке:
    assert pytest.driver.find_element(By.XPATH,
                                      '//span[text()="Необходимо заполнить поле кириллицей. От 2 до 30 символов."]')
