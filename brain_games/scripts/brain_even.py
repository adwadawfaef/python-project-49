#!/usr/bin/env python3
"""Запуск игры «Проверка на чётность»."""

from brain_games import enige
from brain_games.games import even


def main():
    enige.run_game(even)


if __name__ == '__main__':
    main()