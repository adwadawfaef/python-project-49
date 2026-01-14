#!/usr/bin/env python3
"""Модуль для взаимодействия с пользователем."""

import prompt


def welcome_user():
    """
    Приветствует пользователя и спрашивает его имя.
    
    Returns:
        str: Имя пользователя
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name