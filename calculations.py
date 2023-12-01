from __future__ import annotations

import math
import os
import sqlite3

from binarytree import BinaryTree


class Calculation:

    def __init__(self, calc: str, res: str):
        self.__calc = calc
        self.__res = res

    def get_calculation(self) -> str:
        return self.__calc

    def set_calculation(self, calc: str):
        self.__calc = calc

    def get_result(self) -> str:
        return self.__res

    def set_result(self, res: str):
        self.__res = res

    calculation = property(fget=get_calculation, fset=set_calculation)
    result = property(fget=get_result, fset=set_result)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.calculation == other.calculation

    def __str__(self):
        return str(self.__dict__)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError("Comparison with non-Calculation object is not supported.")
        return self.calculation < other.calculation

    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise NotImplementedError("Comparison with non-Calculation object is not supported.")
        return self.calculation > other.calculation


def create_cache_dir():
    try:
        os.mkdir("cache")
    except FileExistsError:
        pass


def create_database_file():
    try:
        f = open("./cache/database.db", "x")
        f.close()
    except FileExistsError:
        pass


create_cache_dir()
create_database_file()
database_connection = sqlite3.connect("./cache/database.db", check_same_thread=False)

calculation_cache: BinaryTree = BinaryTree()


def create_tables():
    database_connection.execute("""
        CREATE TABLE IF NOT EXISTS calculations
        (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            calculation TEXT UNIQUE,
            result      TEXT
        )""")
    database_connection.commit()


def get_result(calc: str) -> Calculation:
    calculation = Calculation(calc=calc, res="")
    search: Calculation | None = calculation_cache.search(calculation)
    if search is None:
        code = eval(compile(str(calc), "<string>", "eval"))
        calculation.result = str(code)
        cache_calculation(calculation)
    else:
        calculation.result = search.result
    print(f"calc {calculation}")
    return calculation


def load_cache():
    res = database_connection.execute("SELECT calculation, result FROM calculations")

    for row in res:
        calc = Calculation(calc=row[0], res=row[1])
        calculation_cache.append(calc)


def cache_calculation(calc: Calculation):
    calculation_cache.append(calc)
    database_connection.execute("INSERT INTO calculations(calculation, result) VALUES (?, ?)",
                                (calc.calculation, calc.result))
    database_connection.commit()


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


fibonacci(99)
