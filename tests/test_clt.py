"""Test CLT."""
import sys
import os

path = os.path.abspath("../")
sys.path.append(path)

import subprocess
from src.app import main
import sqlite3
import os
from unittest.mock import patch


def test_add_patient(capsys):
    # args = ["-f", "db", "--db_function", "add", "--db_level patient"]
    inputs = ["12", "Test Name", "1980-1-1", "123", "test@gmail.com"]
    # main(args)
    # patch("builtins.input", side_effect=inputs)
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
