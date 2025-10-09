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
        email_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.EMAIL)
        )
        assert email_field.is_displayed(), "Поле email не найдено"

        password_field = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.PASSWORD)
        )
        assert password_field.is_displayed(), "Поле пароля не найдено"

        # Проверка наличия кнопки входа
        login_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(Locators.LOGIN)
        )
        assert login_button.is_enabled(), "Кнопка входа не активна"

        # Проверка наличия ссылки на регистрацию
        registration_link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.REGISTRATION)
        )
        assert registration_link.is_displayed(), (
            "Ссылка на регистрацию не найдена"
        )

        # Проверка наличия ссылки на восстановление пароля
        recover_password_link = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(Locators.RECOVER_PASSWORD)
        )
        assert recover_password_link.is_displayed(), (
            "Ссылка на восстановление пароля не найдена"
        )
