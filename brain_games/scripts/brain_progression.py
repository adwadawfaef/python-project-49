#!/usr/bin/env python3
"""Запуск игры «Арифметическая прогрессия»."""

from brain_games.games import progression
from brain_games import enige


def main():
    """Точка входа."""
    enige.run_game(progression)


if __name__ == "__main__":
    main()