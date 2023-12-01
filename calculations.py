from __future__ import annotations

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


def get_result(calc: str) -> Calculation | None:
    return calculation_cache.get(calc, __default=None)

def load_cache():
    calculation_cache.clear()
    database_connection.execute("SELECT calculation, result FROM calculations")

def cache_calculation(calc: Calculation):
    calculation_cache[calc.calculation] = calc
    database_connection.execute("INSERT INTO calculations(calculation, result) VALUES (?, ?)",
                                (calc.calculation, calc.result))
