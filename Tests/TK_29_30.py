import time
import requests
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import settings
from settings import fake_firstname, valid_password, fake_lastname


def test_phone_code_confirmation_old():
    pytest.driver = webdriver.Chrome('C:\\python\\ITOGOVIY MODUL\\chromedriver.exe')
    pytest.driver.implicitly_wait(5)
    pytest.driver.get('https://google.com')
    pytest.driver.execute_script("window.open('about:blank', 'secondtab');")
    pytest.driver.switch_to.window("secondtab")
    pytest.driver.get('https://b2c.passport.rt.ru')
    # Разворачиваем браузер в полноэкранный режим
    pytest.driver.maximize_window()
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')
    real_fake_phone = settings.get_free_phone()
    phone_url = 'https://receive-sms-free.cc/Free-Russia-Phone-Number/' + str(real_fake_phone) + '/'
    # Вводим Имя
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(fake_firstname)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(fake_lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
    real_fake_phone = settings.get_free_phone()
    pytest.driver.find_element(By.XPATH, '//input[@id="address"]').send_keys(real_fake_phone)
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
    # Проверяем, что перешли на страницу Подтверждение телефона
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение телефона"]')
    # получаем код подтверждения
    time.sleep(200)

    pytest.driver.execute_script("window.open('about:blank', 'thirdtab');")
    pytest.driver.switch_to.window("thirdtab")
    pytest.driver.get(phone_url)
    senders = pytest.driver.find_elements(By.XPATH, "//*[@class='col-xs-12 col-md-2']")
    smss = pytest.driver.find_elements(By.XPATH, "//*[@class='col-xs-12 col-md-8']")
    smsarray = []
    for t_row in range(len(senders)):
        temp = []
        temp.append(senders[t_row].text)
        temp.append(smss[t_row].text)
        smsarray.append(temp)
    smscode = ''
    for sms in smsarray:
        if 'Rostelecom' in sms[0]:
            smscode = sms[1]
            break
    reg_code = smscode[smscode.find('Ваш код : ') + len('Ваш код : '):
                       smscode.find('Ваш код : ') + len('Ваш код : ') + 6]
    pytest.driver.switch_to.window("secondtab")
    for i in range(6):
        pytest.driver.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
        pytest.driver.implicitly_wait(3)
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Время жизни кода истекло"]')

def test_email_code_confirmation_old(open_login_page):
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Регистрация"]')
    # получаем емеил
    action = {'action': 'genRandomMailbox', 'count': 1}
    req = requests.get('https://www.1secmail.com/api/v1/', params=action)
    result_email = req.json()[0]
    sign_at = result_email.find('@')
    email_first_part = result_email[:sign_at]
    email_domain = result_email[sign_at+1:]
    # Вводим Имя
    pytest.driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys(fake_firstname)
    pytest.driver.implicitly_wait(5)
    # Вводим фамилию
    pytest.driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys(fake_lastname)
    pytest.driver.implicitly_wait(5)
    # Вводим адрес почты/Email:
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

    # Проверяем, что перешли на страницу Подтверждение почты
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Подтверждение email"]')
    # получаем код подтверждения
    time.sleep(60)
    action = {'action': 'getMessages', 'login': email_first_part, 'domain': email_domain}
    req = requests.get('https://www.1secmail.com/api/v1/', params=action)
    result_id = (req.json()[0]).get('id')
    action = {'action': 'readMessage', 'login': email_first_part, 'domain': email_domain, 'id': result_id}
    res = requests.get('https://www.1secmail.com/api/v1/', params=action)
    email_message = res.json()
    text_body = email_message.get('body')
    reg_code = text_body[text_body.find('Ваш код : ') + len('Ваш код : '):
                         text_body.find('Ваш код : ') + len('Ваш код : ') + 6]
    for i in range(6):
        pytest.driver.find_elements(By.XPATH, '//input[@inputmode="numeric"]')[i].send_keys(reg_code[i])
        pytest.driver.implicitly_wait(3)
    assert pytest.driver.find_element(By.XPATH, '//span[text()="Время жизни кода истекло"]'), 'элемент не найден'
