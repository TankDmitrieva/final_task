from selenium.webdriver.common.by import By
import pytest


def test_design(open_login_page):

    # Нажимаем ссылку Забыл пароль
    pytest.driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    pytest.driver.implicitly_wait(5)
    # Проверяем соответствие дизайна страницы Востановление пароля
    assert pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-phone"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-mail"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-login"]')
    assert pytest.driver.find_element(By.XPATH, '//div[@id="t-btn-tab-ls"]')
    assert pytest.driver.find_element(By.XPATH, '//*[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//*[@id="captcha"]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()=" Далее "]')
    assert pytest.driver.find_element(By.XPATH, '//button[text()=" Вернуться "]')
