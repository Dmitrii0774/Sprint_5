import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators
from ..data import Credentials
from ..curl import login_page, home_page


class TestTransiting:
    """
    Класс для тестирования переходов между разделами приложения
    """

    @pytest.mark.parametrize(
        "locator",
        [Locators.CONSTRUCTOR, Locators.LOGO]
    )
    def test_transition_from_personal_cabinet(self, driver, locator):
        """
        Тест перехода из личного кабинета на главную страницу
        через Конструктор или логотип
        """
        # Шаг 1: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_page)
        )

        # Шаг 2: Авторизация
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 3: Ожидание загрузки личного кабинета
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.PERSONAL_CABINET)
        )

        # Шаг 4: Повторный переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()

        # Шаг 5: Переход через указанный локатор
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(locator)
        )
        driver.find_element(*locator).click()

        # Шаг 6: Проверка перехода на главную страницу
        WebDriverWait(driver, 10).until(
            EC.url_to_be(home_page)
        )
        assert driver.current_url == home_page, (
            f"Ожидаемый URL: {home_page}, "
            f"фактический: {driver.current_url}"
        )
