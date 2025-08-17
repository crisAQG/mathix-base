def abs(x):
    return x if x >= 0 else -x


def frange(start, stop, step=1):
    while start < stop:
        yield start
        start += step


def floor(x):
    i = int(x)
    return i if x >= 0 or x == i else i - 1


def ceil(x):
    i = int(x)
    return i if x == i else i + 1


def gcd(a, b):
    while b: a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a and b else 0


def power(base, exp):
    result = 1
    for _ in range(abs(exp)): result *= base
    return result if exp >= 0 else 1 / result


def sqrt(x, epsilon=1e-1000):
    if x < 0:
        raise ValueError("sqrt no definido para negativos")
    guess = x if x != 0 else 1
    while abs(guess * guess - x) > epsilon:
        guess = (guess + x / guess) / 2
    return guess


def factorial(n):
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    """
    Identifica si n es primo o falso
    """
    if n >= 0:
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    else:
        print("No existen numeros primos negativos")
        return None
