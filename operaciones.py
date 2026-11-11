"""Funciones matemáticas de la calculadora."""

import math


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b


def potencia(base, exponente):
    if base == 0 and exponente < 0:
        raise ValueError("Cero no se puede elevar a un exponente negativo")
    try:
        resultado = base ** exponente
    except OverflowError:
        raise ValueError("El resultado es demasiado grande")
    if isinstance(resultado, complex):
        raise ValueError("El resultado no es un número real")
    return resultado


def modulo(a, b):
    if b == 0:
        raise ValueError("No se puede calcular el módulo con divisor cero")
    return a % b


def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No existe la raíz cuadrada de un número negativo")
    return math.sqrt(n)


def porcentaje(porcentaje, cantidad):
    return porcentaje * cantidad / 100


def valor_absoluto(n):
    return abs(n)


def factorial(n):
    if n < 0 or n != int(n):
        raise ValueError("El factorial solo existe para enteros no negativos")
    return math.factorial(int(n))


def promedio(numeros):
    if len(numeros) == 0:
        raise ValueError("Se necesita al menos un número para el promedio")
    return sum(numeros) / len(numeros)


def redondeo(n, decimales):
    if decimales < 0 or decimales != int(decimales):
        raise ValueError("Los decimales deben ser un entero no negativo")
    return round(n, int(decimales))
