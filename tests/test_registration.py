# Импорты сторонних библиотек
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импорты локальных модулей
from ..locators import Locators
from ..helper import generate_registration_data
from ..data import Credentials
from ..curl import login_page, registration


class TestRegistrationWithNewData:
    """
    Класс для тестирования процесса регистрации с различными типами данных
    """

    def test_registration_valid_data(self, driver):
        """
        Тест успешной регистрации с валидными данными
        """
        name, email, password = generate_registration_data()

        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение формы
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка перехода на страницу входа
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))
        current_url = driver.current_url
        assert login_page in current_url

    def test_registration_invalid_name(self, driver):
        """
        Тест регистрации с пустым именем
        """
        name, email, password = generate_registration_data()

        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение формы с ошибкой
        driver.find_element(*Locators.NAME).send_keys('')
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка оставания на странице регистрации
        WebDriverWait(driver, 5).until(EC.url_to_be(registration))
        current_url = driver.current_url
        assert registration in current_url

    def test_registration_invalid_email(self, driver):
        """
        Тест регистрации с некорректным email
        """
        name, email, password = generate_registration_data()

        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение формы с ошибкой
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys('Arteev.ru')
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка оставания на странице регистрации
        WebDriverWait(driver, 20).until(EC.url_to_be(registration))
        current_url = driver.current_url
        assert registration in current_url

    def test_registration_invalid_password(self, driver):
        """
        Тест регистрации с некорректным паролем
        """
        name, email, password = generate_registration_data()

        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение формы с ошибкой
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys('2w2q')
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Проверка оставания на странице регистрации
        WebDriverWait(driver, 5).until(EC.url_to_be(registration))
        current_url = driver.current_url
        assert registration in current_url

    def test_creation_existing_account(self, driver):
        """
        Тест попытки создания уже существующего аккаунта
        Проверяет, что система корректно отображает ошибку при попытке
        зарегистрировать пользователя с уже существующим email
        """
        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение формы данными существующего пользователя
        driver.find_element(*Locators.NAME).send_keys(Credentials.name)
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Отправка формы
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ожидание появления сообщения об ошибке
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ERROR_REGISTRATION)
        )

        # Проверка текста сообщения об ошибке
        assert error_element.text == 'Такой пользователь уже существует'

    # Параметры для теста подсказки при вводе некорректного пароля
    @pytest.mark.parametrize(
        "invalid_password",
        [
            "1",     # 1 символ
            "12",    # 2 символа
            "123",   # 3 символа
            "1234",  # 4 символа
            "12345"  # 5 символов
        ]
    )
    def test_password_length_hint(self, driver, invalid_password):
        """
        Тест проверки появления подсказки при вводе пароля короче 6 символов
        """
        # Переход к форме регистрации
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Заполнение полей
        driver.find_element(*Locators.NAME).send_keys("Test Name")
        driver.find_element(*Locators.EMAIL).send_keys("test@test.ru")
        password_field = driver.find_element(*Locators.PASSWORD)
        password_field.send_keys(invalid_password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Ожидание появления подсказки об ошибке
        error_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.ERROR_REGISTRATION)
        )

        # Проверка текста ошибки
        assert "Некорректный пароль" in error_element.text
