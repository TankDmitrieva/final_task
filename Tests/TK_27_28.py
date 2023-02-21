import time
import pytest
from selenium.webdriver.common.by import By

import settings
from settings import fake_firstname, valid_password, fake_lastname, fake_email


def test_form_code_confirmation_using_email(open_login_page):
    # Нажимаем ссылку Зарегистрироваться

    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')
    # Вводим Имя
    name = fake_firstname
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(name)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    lastname = fake_lastname
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    femail = fake_email
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(femail)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Проверяем, что перешли на страницу Подтверждения почты
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение email"]')
    # Нажимаем на кнопку изменить email
    pytest.driver.find_element(By.XPATH, '//button[text()="Изменить email"]').click()
    # Проверяем,что перешли на форму ввода регистрационных данных, при этом отображаются все регистрационные данные,
    # которые пользователь ввел до этого
    assert pytest.driver.find_element(By.XPATH,  '//h1[text()="Регистрация"]')
    time.sleep(1)
    list_returned_values = pytest.driver.find_elements(By.XPATH, '//*[@class="rt-input__mask"]')
    returned_values = []
    for element in list_returned_values:
        pytest.driver.execute_script("return arguments[0].innerHTML", element)
        value_text = pytest.driver.execute_script("return arguments[0].textContent", element)
        returned_values.append(value_text)
    assert name == returned_values[0]
    assert lastname == returned_values[1]
    assert femail == returned_values[3]


def test_form_code_confirmation_using_phone(open_login_page):
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')
    # Вводим Имя
    name = fake_firstname
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(name)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    lastname = fake_lastname
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    fnumber = settings.generate_fake_number()
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(fnumber)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Проверяем, что перешли на страницу Подтверждения телефона
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение телефона"]')
    # Нажимаем на кнопку изменить email
    pytest.driver.find_element(By.XPATH, '//button[text()="Изменить номер"]').click()
    # Проверяем,что перешли на форму ввода регистрационных данных, при этом отображаются все регистрационные данные,
    # которые пользователь ввел до этого
    assert pytest.driver.find_element(By.XPATH,  '//h1[text()="Регистрация"]')
    time.sleep(1)
    list_returned_values = pytest.driver.find_elements(By.XPATH, '//*[@class="rt-input__mask"]')
    returned_values = []
    for element in list_returned_values:
        pytest.driver.execute_script("return arguments[0].innerHTML", element)
        value_text = pytest.driver.execute_script("return arguments[0].textContent", element)
        returned_values.append(value_text)
    assert name == returned_values[0]
    assert lastname == returned_values[1]
    assert fnumber == returned_values[3]



