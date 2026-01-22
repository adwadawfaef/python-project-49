#!/usr/bin/env python3
"""Запуск игры «Калькулятор»."""

from brain_games import enige
from brain_games.games import calc

def main():
    enige.run_game(calc)

if __name__ == '__main__':
    main()