from selenium.webdriver.common.by import By
import pytest


def test_design(open_login_page):
    # Нажимаем ссылку Зарегистрироваться
    pytest.driver.find_element(By.XPATH, '//a[text()=" Зарегистрироваться "]').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем, что страница разделена на 2 части
    assert pytest.driver.find_element(By.ID, 'page-left')
    assert pytest.driver.find_element(By.ID, 'page-right')
    # Проверяем, что Имя, Фамилия, Регион, Email или мобильный телефон, Пароль, Подтверждение пароля
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@name="firstName"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@name="lastName"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@autocomplete="new-password"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@id="address"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@id="password"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//input[@id="password-confirm"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()=" Продолжить "]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()=" Политикой конфиденциальности "]')
    assert pytest.driver.find_element(By.XPATH, '//span[text()=" Пользовательским соглашением "]')

    # Проверяем, что Логотип и продуктовый слоган в левой части
    assert pytest.driver.find_element(By.XPATH,
                                      '//section[@id="page-left"]//div[@class="what-is-container__logo-container"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@class="what-is"]')
