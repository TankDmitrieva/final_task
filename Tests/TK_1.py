from selenium.webdriver.common.by import By
import pytest


def test_design(open_login_page):

    # Проверяем, что страница разделена на 2 части
    assert pytest.driver.find_element(By.ID, 'page-left')
    assert pytest.driver.find_element(By.ID, 'page-right')
    # Проверяем, что кнопки Номер, Почта, Логин, Лицевой счет, поле Логина, поле Пароль находятся в левой части
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-phone"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-mail"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-login"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//div[@id="t-btn-tab-ls"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="username"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-left"]//input[@id="password"]')
    # Проверяем, что Логотип и вспомогательная информация находятся в правой части
    assert pytest.driver.find_element(By.XPATH,
                                      '//section[@id="page-right"]//div[@class="what-is-container__logo-container"]')
    assert pytest.driver.find_element(By.XPATH, '//section[@id="page-right"]//div[@class="what-is"]')
