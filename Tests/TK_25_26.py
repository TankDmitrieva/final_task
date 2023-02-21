import pytest
from selenium.webdriver.common.by import By
import settings
from settings import valid_phone, fake_firstname, fake_lastname, valid_password, valid_email, fake_phone


def test_form_code_confirmation_using_phone(open_login_page):

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
    fake_phone = settings.generate_fake_number()
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(fake_phone)
    pytest.driver.implicitly_wait(3)
    # Вводим пароль:
    pytest.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Вводим подтверждение пароля:
    pytest.driver.find_element(By.XPATH, '//input[@id="password-confirm"]').send_keys(valid_password)
    pytest.driver.implicitly_wait(3)
    # Нажимаем на кнопку 'Зарегистрироваться':
    pytest.driver.find_element(By.XPATH, '//button[text()=" Зарегистрироваться "]').click()
    # Проверяем, что перешли на страницу Подтверждение телефона
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение телефона"]')

    # Проверяем, что на странице находятся замаскированный номер телефона,поля для ввода кода,
    # кнопку "Получить код повторно", кнопку "Изменить номер"

    assert '*' in pytest.driver.find_element(By.XPATH, '//p[@class="register-confirm-form-container__desc"]').text
    assert pytest.driver.find_element(By.XPATH, '//div[@class="sdi-container sdi-container--medium"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()="Получить код повторно"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()="Изменить номер"]')





def test_form_code_confirmation_using_email(open_login_page):

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
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(settings.fake_email)
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


    # Проверяем, что на странице находятся замаскированная почта,поля для ввода кода,
    # кнопку "Получить код повторно", кнопку "Изменить почта"

    assert '*' in pytest.driver.find_element(By.XPATH, '//p[@class="register-confirm-form-container__desc"]').text
    assert pytest.driver.find_element(By.XPATH, '//div[@class="sdi-container sdi-container--medium"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()="Получить код повторно"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()="Изменить почта"]')
