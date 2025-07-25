# Импорты сторонних библиотек
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Импорты локальных модулей
from ..curl import home_page, login_page
from ..data import Credentials
from ..locators import Locators


@pytest.fixture(scope="function")
def driver():
    """
    Фиксатура для инициализации драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(home_page)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture(scope="function")
def authorized(driver):
    """
    Фиксатура для авторизации пользователя
    """
    # Переход в личный кабинет
    driver.find_element(*Locators.PERSONAL_CABINET).click()
    WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

    # Ввод учетных данных
    driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
    driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

    # Авторизация
    driver.find_element(*Locators.LOGIN).click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(Locators.PERSONAL_CABINET)
    )

    return driver
