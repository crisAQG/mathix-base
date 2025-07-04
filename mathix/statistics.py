from mathix.discrete_probability import *
from mathix.algebra import *


def binomial_probability(n, k, p):
    return combinations(n, k) * power(p, k) * power(1 - p, n - k)


def normal_pdf(x, mean=0, std=1):
    pi = 3.141592653589793
    return (1 / (std * sqrt(2 * pi))) * exp(-0.5 * power((x - mean) / std, 2))


def mean(data):
    return sum(data) / len(data)


def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def median(data):
    data = sorted(data)
    n = len(data)
    return (data[n // 2 - 1] + data[n // 2]) / 2 if n % 2 == 0 else data[n // 2]
