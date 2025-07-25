# Импорты сторонних библиотек
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Импорты локальных модулей
from ..locators import Locators
from ..data import Credentials
from ..curl import login_page, home_page, forgot_page, reset


class TestEntry:
    """
    Класс для тестирования процесса авторизации в системе
    """

    def test_valid_entry_via_personal_account(self, driver):
        """
        Тест успешной авторизации через кнопку "Личный кабинет"

        Шаги:
        1. Переход в личный кабинет
        2. Ввод учетных данных
        3. Авторизация
        4. Проверка успешной авторизации
        """
        # Шаг 1: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод учетных данных
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Шаг 3: Авторизация
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN)
            )
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка успешной авторизации
        WebDriverWait(driver, 10).until(EC.url_to_be(home_page))
        current_url = driver.current_url
        assert home_page == current_url, (
            f"Ожидаемый URL: {home_page}, "
            f"фактический: {current_url}"
        )

    def test_valid_entry_via_login_to_account(self, driver):
        """
        Тест успешной авторизации через кнопку "Войти в аккаунт"

        Шаги:
        1. Переход через кнопку "Войти в аккаунт"
        2. Ввод учетных данных
        3. Авторизация
        4. Проверка успешной авторизации
        """
        # Шаг 1: Переход через кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод учетных данных
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Шаг 3: Авторизация
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN)
            )
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка успешной авторизации
        WebDriverWait(driver, 10).until(EC.url_to_be(home_page))
        current_url = driver.current_url
        assert home_page == current_url, (
            f"Ожидаемый URL: {home_page}, "
            f" фактический: {current_url}"
        )

    def test_valid_entry_via_recover_password(self, driver):
        """
        Тест восстановления пароля

        Шаги:
        1. Переход к форме входа
        2. Переход к форме восстановления пароля
        3. Ввод email
        4. Отправка формы
        5. Проверка перехода на страницу сброса пароля
        """
        # Шаг 1: Переход к форме входа
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()

        # Шаг 2: Переход к форме восстановления пароля
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(forgot_page))

        # Шаг 3: Ввод email
        driver.find_element(*Locators.EMAIL_FOR_RECOVERY).send_keys(
            Credentials.email
        )

        # Шаг 4: Отправка формы
        driver.find_element(*Locators.RECOVER_BUTTON).click()

        # Шаг 5: Проверка перехода
        WebDriverWait(driver, 5).until(EC.url_to_be(reset))
        current_url = driver.current_url
        assert reset in current_url, (
            f"Ожидаемый URL: {reset}, "
            f"фактический: {current_url}"
        )

    def test_valid_entry_via_registration(self, driver):
        """
        Тест регистрации нового пользователя

        Шаги:
        1. Переход к форме регистрации
        2. Подтверждение регистрации
        3. Вход в систему
        4. Проверка успешной авторизации
        """
        # Шаг 1: Переход к форме регистрации
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Шаг 2: Подтверждение регистрации
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 3: Вход в систему
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.LOGIN)
        )
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка успешной авторизации
        WebDriverWait(driver, 10).until(EC.url_to_be(home_page))
        current_url = driver.current_url
        assert home_page == current_url, (
            f"Ожидаемый URL: {home_page}, "
            f"фактический: {current_url}"
        )

    def test_entry_via_personal_account_invalid_email(self, driver):
        """
        Тест авторизации с некорректным email через личный кабинет

        Шаги:
        1. Переход в личный кабинет
        2. Ввод некорректного email
        3. Попытка авторизации
        4. Проверка результата
        """
        # Шаг 1: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 20).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод некорректных данных
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Шаг 3: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка результата
        current_url = driver.current_url
        assert login_page in current_url, (
            f"Ожидаемый URL: {login_page}, "
            f"фактический: {current_url}"
        )

    def test_entry_via_personal_account_invalid_password(self, driver):
        """
        Тест авторизации с некорректным паролем через личный кабинет

        Шаги:
        1. Переход в личный кабинет
        2. Ввод корректного email
        3. Ввод некорректного пароля
        4. Попытка авторизации
        5. Проверка сообщения об ошибке
        """
        # Шаг 1: Переход в личный кабинет
        driver.find_element(*Locators.PERSONAL_CABINET).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод данных
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')

        # Шаг 3: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка сообщения об ошибке
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text, (
            f"Ожидаемое сообщение: 'Некорректный пароль', "
            f"фактическое: {error_text}"
        )

    def test_entry_via_login_to_account_invalid_email(self, driver):
        """
        Тест авторизации с некорректным email через кнопку "Войти в аккаунт"

        Шаги:
        1. Переход через кнопку "Войти в аккаунт"
        2. Ввод некорректного email
        3. Попытка авторизации
        4. Проверка результата
        """
        # Шаг 1: Переход через кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод некорректных данных
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Шаг 3: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка результата
        current_url = driver.current_url
        assert login_page in current_url, (
            f"Ожидаемый URL: {login_page}, "
            f"фактический: {current_url}"
        )

    def test_entry_via_login_to_account_invalid_password(self, driver):
        """
        Тест авторизации с некорректным паролем через кнопку "Войти в аккаунт"

        Шаги:
        1. Переход через кнопку "Войти в аккаунт"
        2. Ввод корректного email
        3. Ввод некорректного пароля
        4. Попытка авторизации
        5. Проверка сообщения об ошибке
        """
        # Шаг 1: Переход через кнопку "Войти в аккаунт"
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 2: Ввод данных
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)
        driver.find_element(*Locators.PASSWORD).send_keys('123')

        # Шаг 3: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 4: Проверка сообщения об ошибке
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text, (
            f"Ожидаемое сообщение: 'Некорректный пароль', "
            f"фактическое: {error_text}"
        )

    def test_entry_via_recover_password_invalid_email(self, driver):
        """
        Тест восстановления пароля с некорректным email

        Шаги:
        1. Переход к форме восстановления
        2. Ввод некорректного email
        3. Попытка отправки формы
        4. Проверка результата
        """
        # Шаг 1: Переход к форме восстановления
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(forgot_page))

        # Шаг 2: Ввод некорректных данных
        driver.find_element(*Locators.EMAIL_FOR_RECOVERY).send_keys(
            'Некорректный адрес'
        )

        # Шаг 3: Попытка отправки формы
        driver.find_element(*Locators.RECOVER_BUTTON).click()

        # Шаг 4: Проверка результата
        current_url = driver.current_url
        assert forgot_page in current_url, (
            f"Ожидаемый URL: {forgot_page}, "
            f"фактический: {current_url}"
        )

    def test_entry_via_registration_invalid_email(self, driver):
        """
        Тест регистрации с некорректным email

        Шаги:
        1. Переход к форме регистрации
        2. Подтверждение регистрации
        3. Ввод некорректного email
        4. Попытка авторизации
        5. Проверка результата
        """
        # Шаг 1: Переход к форме регистрации
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Шаг 2: Подтверждение регистрации
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 3: Ввод некорректных данных
        driver.find_element(*Locators.EMAIL).send_keys('Некорректный адрес')
        driver.find_element(*Locators.PASSWORD).send_keys(Credentials.password)

        # Шаг 4: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 5: Проверка результата
        current_url = driver.current_url
        assert login_page in current_url, (
            f"Ожидаемый URL: {login_page}, "
            f"фактический: {current_url}"
        )

    def test_entry_via_registration_invalid_password(self, driver):
        """
        Тест регистрации с некорректным паролем

        Шаги:
        1. Переход к форме регистрации
        2. Подтверждение регистрации
        3. Ввод корректного email
        4. Ввод некорректного пароля
        5. Попытка авторизации
        6. Проверка сообщения об ошибке
        """
        # Шаг 1: Переход к форме регистрации
        driver.find_element(*Locators.LOGIN_TO_ACCOUNT).click()
        driver.find_element(*Locators.REGISTRATION).click()

        # Шаг 2: Подтверждение регистрации
        driver.find_element(*Locators.REGISTERED_LOGIN).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_page))

        # Шаг 3: Ввод корректного email
        driver.find_element(*Locators.EMAIL).send_keys(Credentials.email)

        # Шаг 4: Ввод некорректного пароля
        driver.find_element(*Locators.PASSWORD).send_keys('123')

        # Шаг 5: Попытка авторизации
        driver.find_element(*Locators.LOGIN).click()

        # Шаг 6: Проверка сообщения об ошибке
        error_text = driver.find_element(*Locators.ERROR_REGISTRATION).text
        assert 'Некорректный пароль' in error_text, (
            f"Ожидаемое сообщение: 'Некорректный пароль', "
            f"фактическое: {error_text}"
        )
