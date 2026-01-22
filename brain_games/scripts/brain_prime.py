#!/usr/bin/env python3
"""Запуск игры «Простое ли число?»."""

from brain_games import enige
from brain_games.games import prime


def main():
    enige.run_game(prime)


if __name__ == '__main__':
    main()
