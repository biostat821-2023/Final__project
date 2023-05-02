"""Test CLT."""
import sys
import os

path = os.path.abspath(".")
sys.path.append(path)

import subprocess  # noqa: E402
from src.app import main  # noqa: E402
import sqlite3  # noqa: E402


def test_add_patient(capsys):
    inputs = ["12", "Test Name", "Male", "1980-1-1", "123", "test@gmail.com"]
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "add",
        "--db_level",
        "patient",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    stdout, _ = process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Patient where Patient_id = '12'")
    res = c.fetchall()
    assert res[0][0] == "12"
    assert res[0][1] == "Test Name"
    assert res[0][2] == "Male"
    assert res[0][3] == "1980-01-01 00:00:00"
    assert res[0][4] == 43
    assert res[0][5] == 123
    assert res[0][6] == "test@gmail.com"
    conn.close()
    os.remove("database.db")


def test_add_sample(capsys):
    inputs = [
        "12",
        "abc",
        "2019-3-3",
        "Breast Invasive Carcinoma",
        "9",
        "No",
        "1.5",
    ]
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "add",
        "--db_level",
        "sample",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    stdout, _ = process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Sample where Sample_id = 'abc'")
    res = c.fetchall()
    assert res[0][0] == "abc"
    assert res[0][1] == "12"
    assert res[0][2] == "2019-03-03 00:00:00"
    assert res[0][3] == "Breast Invasive Carcinoma"
    assert res[0][4] == 9
    assert res[0][5] == "No"
    assert res[0][6] == 1.5
    conn.close()
    os.remove("database.db")
