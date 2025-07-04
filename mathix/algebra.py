from mathix.arithmetic import *


def exp(x, terms=20):
    return sum(power(x, n) / factorial(n) for n in range(terms))

def log(x, base=2.718281828459045, terms=100):
    if x <= 0: raise ValueError("log indefinido")
    n = 0
    while x > 2: x /= base; n += 1
    x -= 1
    return sum(power(-1, i + 1) * power(x, i) / i for i in range(1, terms)) + n

def solve_quadratic(a, b, c):
    disc = power(b, 2) - 4 * a * c
    if disc < 0: return []
    sqrt_disc = sqrt(disc)
    return [(-b + sqrt_disc) / (2 * a), (-b - sqrt_disc) / (2 * a)] if disc > 0 else [-b / (2 * a)]

def simplify_addition(expr):
    terms = expr.replace('-', '+-').split('+')
    numeric = sum(float(t) for t in terms if t.strip().replace('.', '', 1).lstrip('-').isdigit())
    symbols = [t for t in terms if not t.strip().replace('.', '', 1).lstrip('-').isdigit()]
    return f"{numeric}" + (" + " + " + ".join(symbols) if symbols else '')
