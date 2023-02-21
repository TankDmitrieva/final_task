from selenium.webdriver.common.by import By
import pytest


def test_btn_terms_of_use(open_login_page):

    # Нажимаем кнопку Пользовательское соглашение
    pytest.driver.find_element(By.XPATH, '//a[text()="пользовательского соглашения"]').click()
    # Переключаемся на новую вкладку
    window_after = pytest.driver.window_handles[1]
    pytest.driver.switch_to.window(window_after)
    # Проверяем, что переадресация на страницу Публичная оферта
    assert pytest.driver.find_element(By.XPATH, '//title[text()="User agreement"]')
