#!/usr/bin/env python3
"""Игра «Калькулятор»."""

import operator
import random

DESCRIPTION = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 50

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


def calculate(num1, num2, operation):
    return OPERATIONS[operation](num1, num2)


def generate_question_and_answer():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    operation = random.choice(list(OPERATIONS.keys()))

    question = f'{num1} {operation} {num2}'
    correct_answer = calculate(num1, num2, operation)

    return question, correct_answer