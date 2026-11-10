"""Funciones matemáticas de la calculadora."""

import math


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def potencia(base, exponente):
    return base ** exponente


def modulo(a, b):
    return a % b


def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No existe la raíz cuadrada de un número negativo")
    return math.sqrt(n)
