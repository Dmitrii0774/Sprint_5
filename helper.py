from faker import Faker
import random

faker = Faker()


def generate_registration_data():
    """
    Генерирует валидные данные для регистрации пользователя
    Формирует уникальное имя, email и пароль согласно требованиям
    """
    # Генерация имени
    name = faker.first_name() + ' ' + faker.last_name()

    # Генерация уникального email
    first_name = faker.first_name().lower()
    last_name = faker.last_name().lower()
    cohort_number = random.randint(1, 99)  # номер когорты
    random_digits = random.randint(100, 999)  # случайные 3 цифры
    domain = random.choice(['yandex.ru', 'gmail.com', 'mail.ru'])

    email = (
        f"{first_name}_{last_name}_{cohort_number}_{random_digits}"
        f"@{domain}"
    )

    # Генерация пароля (минимум 6 символов)
    password = faker.password(
        length=random.randint(6, 12),  # случайная длина от 6 до 12 символов
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True
    )

    return name, email, password
