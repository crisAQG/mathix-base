from mathix.arithmetic import *


def sin(x, terms=11):
    x %= 2 * 3.141592653589793
    result = 0
    for n in range(terms):
        sign = -1 if n % 2 else 1
        result += sign * power(x, 2 * n + 1) / factorial(2 * n + 1)
    return result

def cos(x, terms=12):
    x %= 2 * 3.141592653589793
    result = 0
    for n in range(terms):
        sign = -1 if n % 2 else 1
        result += sign * power(x, 2 * n) / factorial(2 * n)
    return result

def tan(x):
    c = cos(x)
    if c == 0: raise ValueError("tan indefinido")
    return sin(x) / c

def arcsin(x, terms=11):
    if x < -1 or x > 1: raise ValueError("arcsin fuera de dominio")
    result = x
    num = x
    for n in range(1, terms):
        num *= x * x
        result += (factorial(2 * n) * num) / (power(4, n) * power(factorial(n), 2) * (2 * n + 1))
    return result

def arccos(x, terms=11):
    return 3.141592653589793 / 2 - arcsin(x, terms)

def arctan(x, terms=11):
    result = 0
    for n in range(terms):
        sign = -1 if n % 2 else 1
        result += sign * power(x, 2 * n + 1) / (2 * n + 1)
    return result
