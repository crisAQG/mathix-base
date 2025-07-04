from mathix.arithmetic import *


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def permutations(n, r):
    return factorial(n) // factorial(n - r)
