from __future__ import annotations

import math
from fractions import Fraction

import data
from binarytree import BinaryTree
from calculation import Calculation

calculation_cache: BinaryTree = BinaryTree()


def load_cache():
    for calc in data.get_calculations():
        calculation_cache.append(calc)

    fibonacci(99)
    fac(99)


def get_result(calc: str) -> Calculation:
    calculation = Calculation(calc=calc, res="")
    search: Calculation | None = calculation_cache.search(calculation)
    if search is None:
        code = eval(compile(str(calc), "<string>", "eval"))
        calculation.result = str(code)
        data.cache_calculation(calculation)
        calculation_cache.append(calculation)
    else:
        calculation.result = search.result
    print(f"calc {calculation}")
    return calculation


def to_fraction(x: float) -> str:
    return str(Fraction(float(x)).limit_denominator())


def is_float(x: str) -> bool:
    try:
        float(x)
        return True
    except ValueError:
        return False


fib_cache = {
    0: 0,
    1: 1
}

fac_cache = {
    0: 1,
    1: 1
}

pi = math.pi
e = math.e


def root(x, y):
    return math.pow(x, 1 / y)


def pow(x, y):
    return math.pow(x, y)


def sin(x):
    return math.sin(x)


def cos(x):
    return math.cos(x)


def tan(x):
    return math.tan(x)


def asin(x):
    return math.asin(x)


def acos(x):
    return math.acos(x)


def atan(x):
    return math.atan(x)


def ln(x):
    return math.log(x, e)


def log(x, base):
    return math.log(x, base)


def fac(x):
    fc = 1
    for i in range(x + 1):
        if i in fac_cache:
            fc = fac_cache[i]
        else:
            fc *= i
            fac_cache[i] = fc
    return fc


def fibonacci(n):
    if n in fib_cache:
        return fib_cache.get(n)
    n1 = fibonacci(n - 1)
    n2 = fibonacci(n - 2)

    fib_cache[n - 1] = n1
    fib_cache[n - 2] = n2

    return n1 + n2
