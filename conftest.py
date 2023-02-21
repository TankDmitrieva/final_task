import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(autouse=True)
def open_login_page():
   pytest.driver = webdriver.Chrome('C:\\python\\ITOGOVIY MODUL\\chromedriver.exe')
   # Устанавливаем не явное ожидание
   pytest.driver.implicitly_wait(5)
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru')
   # Разворачиваем браузер в полноэкранный режим
   pytest.driver.maximize_window()

   yield

   pytest.driver.quit()
