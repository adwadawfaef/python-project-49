### Hexlet tests and linter status:
[![Actions Status](https://github.com/adwadawfaef/python-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/adwadawfaef/python-project-49/actions)

## Clone project
git clone https://github.com/adwadawfaef/python-project-49

## Технолоджия
* **Python 3.8+**
* **UV** - быстрый менеджер пакетов Python
* **Ruff** - линтер для Python
* **Prompt** - библиотека для ввода пользователя

## Установить все необходимые пакеты
make build
make package-install
Или в ручную с помощью uv (установить его можно по ссылке: https://docs.astral.sh/uv/)
uv build
uv tool install dist/*.whl

## Activate /venv
source .venv/bin/activate

## Build game
**make build**

## Игры

1. **brain-even** - Определить чётное ли число
2. **brain-calc** - Вычислить выражение
3. **brain-gcd** - Найти наибольший общий делитель
4. **brain-progression** - Найти пропущенное число в прогрессии
5. **brain-prime** - Определить простое ли число

## Запуск игр:

1. **brain-even**
2. **brain-calc**
3. **brain-gcd**
4. **brain-progression**
5. **brain-prime**

## ascinema

### even
[![asciicast](https://asciinema.org/a/azazkHoIcB5UwopM.svg)](https://asciinema.org/a/azazkHoIcB5UwopM)

### calc
[![asciicast](https://asciinema.org/a/M7ToFe9TpWo0ngc0.svg)](https://asciinema.org/a/M7ToFe9TpWo0ngc0)

### gcd
[![asciicast](https://asciinema.org/a/MwCo7aTm4u9irHXp.svg)](https://asciinema.org/a/MwCo7aTm4u9irHXp)

### brain-progression
[![asciicast](https://asciinema.org/a/aKnvZoGh9dUzd9oe.svg)](https://asciinema.org/a/aKnvZoGh9dUzd9oe)

### brain-prime
[![asciicast](https://asciinema.org/a/FyxQNmpGtPeNcOIn.svg)](https://asciinema.org/a/FyxQNmpGtPeNcOIn)

## В чём суть каждой игры

* **brain-even** — Определить, является ли случайное число чётным (делится на 2 без остатка)
* **brain-calc** — Вычислить результат математического выражения со случайными числами и операциями (+, -, *)
* **brain-gcd** — Найти наибольший общий делитель двух случайных чисел
* **brain-progression** — Найти пропущенное число в арифметической прогрессии
* **brain-prime** — Определить, является ли случайное число простым (имеет ровно два делителя: 1 и само себя)

## Структура проекта
brain_games/
├── engine.py # Общий движок
├── games/ # Логика конкретных игр
│ ├── even.py # Проверка на чётность
│ ├── calc.py # Калькулятор (+,-,*)
│ ├── gcd.py # Наибольший общий делитель
│ ├── progression.py # Арифметическая прогрессия
│ └── prime.py # Проверка на простоту
└── scripts/ # Точки входа
├── brain_even.py
├── brain_calc.py
├── brain_gcd.py
├── brain_progression.py
└── brain_prime.py
