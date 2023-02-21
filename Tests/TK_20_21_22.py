import time
from selenium.webdriver.common.by import By
import pytest
from settings import valid_email, fake_firstname, fake_lastname, valid_password
import requests


def test_registration_valid(open_login_page): # ?? проблемы с приходом письма с кодом. нужно тестить

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
    # Получаем валидный случайный email и разделяем его на части для дальнейших запросов
    action = {'action': 'genRandomMailbox', 'count': 1}
    req = requests.get('https://www.1secmail.com/api/v1/', params=action)
    result_email = req.json()[0]
    sign_at = result_email.find('@')
    email_first_part = result_email[:sign_at]
    email_domain = result_email[sign_at+1:]

    # Вводим полученный адрес почты
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(result_email)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    time.sleep(30)

    #Получаем код из сгенерированной ранее почты
    action = {'action': 'getMessages', 'login': email_first_part, 'domain': email_domain}
    req = requests.get('https://www.1secmail.com/api/v1/', params=action)
    result_id = (req.json()[0]).get('id')
    action = {'action': 'readMessage', 'login': email_first_part, 'domain': email_domain, 'id': result_id}
    res = requests.get('https://www.1secmail.com/api/v1/', params=action)
    email_message = res.json()
    text_body = email_message.get('body')
    reg_code = text_body[text_body.find('Ваш код : ') + len('Ваш код : '):
                         text_body.find('Ваш код : ') + len('Ваш код : ') + 6]

    # Вводим полученный код
    for i in range(6):
        pytest.driver.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
        pytest.driver.implicitly_wait(3)
    assert pytest.driver.find_element(By.XPATH, '//*[@id="logout-btn"]')


def test_registration_with_used_email_redirect_auth(open_login_page):

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
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
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


def test_registration_with_used_email_restore_password(open_login_page):

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
        pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(valid_email)
        pytest.driver.implicitly_wait(3)
        # Вводим пароль:
        pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
        pytest.driver.implicitly_wait(3)
        # Вводим подтверждение пароля:
        pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
        pytest.driver.implicitly_wait(3)
        # Нажимаем на кнопку 'Зарегистрироваться':
        pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
        # Нажимаем на кнопку 'Востановить пароль'
        pytest.driver.find_element(By.XPATH, '//a[text()=" Восстановить пароль "]').click()
        # Проверяем, что перешли на страницу Востановление пароля
        assert pytest.driver.find_element(By.XPATH, '//h1[text()="Восстановление пароля"]')
