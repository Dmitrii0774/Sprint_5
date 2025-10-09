from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..curl import login_page, account_page
from ..data import Credentials
from ..locators import Locators


class TestExit:
    """
    Класс для тестирования функционала выхода из личного кабинета
    """

    def test_exit(self, driver):
        """
        Тест проверки корректности выхода из личного кабинета

        Шаги теста:
        1. Переход на страницу авторизации
        2. Вход в систему
        3. Переход в личный кабинет
        4. Выполнение выхода
        5. Проверка успешной авторизации
        """

        # Шаг 1: Переход на страницу авторизации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(login_page))

        # Шаг 2: Авторизация в системе
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()

        # Проверка успешной авторизации
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.PERSONAL_CABINET)
        )

        # Шаг 3: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(account_page))

        # Шаг 4: Выполнение выхода из системы
        driver.find_element(*Locators.EXIT).click()

        # Шаг 5: Проверка успешной авторизации
        WebDriverWait(driver, 10).until(EC.url_to_be(login_page))

        # Финальная проверка URL
        current_url = driver.current_url
        assert login_page in current_url, \
            f"Ожидаемый URL: {login_page}, фактический: {current_url}"
