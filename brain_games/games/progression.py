import random

DESCRIPTION = 'What number is missing in the progression?'

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 50
MIN_STEP = 1
MAX_STEP = 10


def generate_progression(start, step, length):
    """
    Генерирует арифметическую прогрессию.

    Args:
        start: первое число прогрессии
        step: шаг прогрессии
        length: длина прогрессии

    Returns:
        Список чисел прогрессии
    """
    return [start + i * step for i in range(length)]


def generate_question_and_answer():
    """
    Генерирует прогрессию с одним скрытым элементом.

    Returns:
        Кортеж (вопрос, правильный_ответ)
    """
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    hidden_index = random.randint(0, length - 1)

    progression = generate_progression(start, step, length)

    # Запоминаем скрытое число
    hidden_number = progression[hidden_index]

    # Заменяем скрытое число на ".."
    progression[hidden_index] = '..'

    # Формируем вопрос
    question = ' '.join(map(str, progression))

    return question, hidden_number