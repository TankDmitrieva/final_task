from selenium.webdriver.common.by import By
import pytest


def test_password(open_login_page):

    # Нажимаем ссылку Забыл пароль
    pytest.driver.find_element(By.XPATH, '//*[@id="forgot_password"]').click()
    pytest.driver.implicitly_wait(10)
    # Проверяем, что переадресация на страницу восстановления пароля
    assert pytest.driver.find_element(By.XPATH, '//h1[text()="Восстановление пароля"]')
