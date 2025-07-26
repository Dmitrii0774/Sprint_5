# Сторонние библиотеки
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Локальные импорты
from ..locators import Locators


class TestConstructor:
    """
    Класс для тестирования переходов между разделами конструктора
    бургеров
    """

    def test_transition_to_sauces(self, driver):
        """
        Тест перехода в раздел соусов
        Шаги:
        1. Переход в раздел соусов
        2. Проверка активности секции
        3. Проверка названия активной секции
        """
        # Шаг 1: Переход в раздел соусов
        driver.find_element(*Locators.SAUCES).click()

        # Шаг 2: Проверка активности секции
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )

        # Шаг 3: Проверка названия
        assert "current" in active_section.get_attribute("class"), (
            f"Ожидаемый класс 'current', "
            f"фактический: {active_section.get_attribute('class')}"
        )
        assert active_section.text == "Соусы", (
            f"Ожидаемое название: 'Соусы', "
            f"фактическое: {active_section.text}"
        )

    def test_transition_to_fillings(self, driver):
        """
        Тест перехода в раздел начинок
        Шаги:
        1. Переход в раздел начинок
        2. Проверка активности секции
        3. Проверка названия активной секции
        """
        # Шаг 1: Переход в раздел начинок
        driver.find_element(*Locators.FILLINGS).click()

        # Шаг 2: Проверка активности секции
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )

        # Шаг 3: Проверка названия
        assert "current" in active_section.get_attribute("class"), (
            f"Ожидаемый класс 'current', "
            f"фактический: {active_section.get_attribute('class')}"
        )
        assert active_section.text == "Начинки", (
            f"Ожидаемое название: 'Начинки', "
            f"фактическое: {active_section.text}"
        )

    def test_transition_to_buns(self, driver):
        """
        Тест перехода в раздел булок
        Шаги:
        1. Переход в раздел начинок (предварительный)
        2. Переход в раздел булок
        3. Проверка активности секции
        4. Проверка названия активной секции
        """
        # Шаг 1: Переход в раздел начинок
        driver.find_element(*Locators.FILLINGS).click()

        # Шаг 2: Переход в раздел булок
        driver.find_element(*Locators.BUNS).click()

        # Шаг 3: Проверка активности секции
        active_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.ACTIVE_SECTION)
        )

        # Шаг 4: Проверка названия
        assert "current" in active_section.get_attribute("class"), (
            f"Ожидаемый класс 'current', "
            f"фактический: {active_section.get_attribute('class')}"
        )
        assert active_section.text == "Булки", (
            f"Ожидаемое название: 'Булки', "
            f"фактическое: {active_section.text}"
        )
