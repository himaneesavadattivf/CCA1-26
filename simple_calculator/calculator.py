"""Simple calculator functions."""

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b


def power(a, b):
    return a ** b


def mod(a, b):
    return a % b


__all__ = ["add", "subtract", "multiply", "divide", "power", "mod"]
