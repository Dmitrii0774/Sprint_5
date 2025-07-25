from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..curl import login_page, home_page
from ..locators import Locators


class TestPersonalCabinet:
    """
    Класс для тестирования работы с личным кабинетом
    """

    def test_transition_to_personal_cabinet(self, driver):
        """
        Тест перехода в личный кабинет

        Шаги:
        1. Открытие главной страницы
        2. Переход в личный кабинет
        3. Проверка перехода на страницу авторизации
        4. Проверка элементов формы авторизации
        """
        # Шаг 1: Открытие главной страницы
        driver.get(home_page)

        # Шаг 2: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()

        # Шаг 3: Проверка перехода на страницу авторизации
        WebDriverWait(driver, 10).until(
            EC.url_to_be(login_page)
        )

        # Шаг 4: Проверка элементов формы авторизации
        # Проверка наличия полей ввода
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL)
        )
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.PASSWORD)
        )

        # Проверка наличия кнопки входа
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN)
        )

        # Проверка наличия ссылки на регистрацию
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.REGISTRATION)
        )

        # Проверка наличия ссылки на восстановление пароля
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.RECOVER_PASSWORD)
        )
