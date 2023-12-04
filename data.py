import os
import sqlite3

from calculation import Calculation


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


def create_tables():
    database_connection.execute("""
        CREATE TABLE IF NOT EXISTS calculations
        (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            calculation TEXT UNIQUE,
            result      TEXT
        )""")
    database_connection.commit()


def get_calculations() -> list[Calculation]:
    res = database_connection.execute("SELECT calculation, result FROM calculations")

    results: list[Calculation] = []

    for row in res:
        calc = Calculation(calc=row[0], res=row[1])
        results.append(calc)
    return results


def cache_calculation(calc: Calculation):
    database_connection.execute("INSERT INTO calculations(calculation, result) VALUES (?, ?)",
                                (calc.calculation, calc.result))
    database_connection.commit()
