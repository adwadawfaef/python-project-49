#!/usr/bin/env python3
"""Запуск игры «Проверка на чётность»."""

from brain_games.games import brain_even
from brain_games import enige


def main():
    """Точка входа."""
    enige.run_game(brain_even)


if __name__ == "__main__":
    main()