#!/usr/bin/env python3
"""Запуск игры «Калькулятор»."""

from brain_games.games import brain_calc
from brain_games.games import brain_even


def main():
    """Точка входа."""
    brain_even.run_game(brain_calc)


if __name__ == "__main__":
    main()