#!/usr/bin/env python3
"""Запуск игры «Наибольший общий делитель (НОД)»."""

from brain_games import enige
from brain_games.games import gcd


def main():
    enige.run_game(gcd)


if __name__ == '__main__':
    main()