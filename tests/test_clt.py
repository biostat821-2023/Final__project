"""Test CLT."""
import sys
import os

path = os.path.abspath(".")
sys.path.append(path)

import subprocess  # noqa: E402
import sqlite3  # noqa: E402


def test_add_patient(capsys):  # pylint: disable=W0613
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
    process.communicate("\n".join(inputs))
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
    # os.remove("database.db")


def test_add_sample(capsys):  # pylint: disable=W0613
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
    process.communicate("\n".join(inputs))
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
    # os.remove("database.db")


def test_update_patient(capsys):  # pylint: disable=W0613
    inputs = ["12", "Test Name", "Male", "1980-1-1", "12345", "test2@gmail.com"]  # noqa
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "update",
        "--db_level",
        "patient",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Patient where Patient_id = '12'")
    res = c.fetchall()
    assert res[0][0] == "12"
    assert res[0][1] == "Test Name"
    assert res[0][2] == "Male"
    assert res[0][3] == "1980-01-01 00:00:00"
    assert res[0][4] == 43
    assert res[0][5] == 12345
    assert res[0][6] == "test2@gmail.com"
    conn.close()
    # os.remove("database.db")


def test_update_sample(capsys):  # pylint: disable=W0613
    inputs = [
        "12",
        "abc",
        "2019-3-4",
        "Breast Invasive Carcinoma",
        "9",
        "No",
        "1.6",
    ]
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "update",
        "--db_level",
        "sample",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Sample where Sample_id = 'abc'")
    res = c.fetchall()
    assert res[0][0] == "abc"
    assert res[0][1] == "12"
    assert res[0][2] == "2019-03-04 00:00:00"
    assert res[0][3] == "Breast Invasive Carcinoma"
    assert res[0][4] == 9
    assert res[0][5] == "No"
    assert res[0][6] == 1.6
    conn.close()
    # os.remove("database.db")


def test_delete_sample(capsys):  # pylint: disable=W0613
    inputs = ["abc"]
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "delete",
        "--db_level",
        "sample",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Sample where Sample_id = 'abc'")
    res = c.fetchall()
    assert len(res) == 0
    conn.close()
    # os.remove("database.db")


def test_delete_patient(capsys):  # pylint: disable=W0613
    inputs = ["12"]
    commands = [
        "python",
        "src/app.py",
        "-f",
        "db",
        "--db_function",
        "delete",
        "--db_level",
        "patient",
    ]
    process = subprocess.Popen(
        commands, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
    )
    process.communicate("\n".join(inputs))
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Patient where Patient_id = '12'")
    res = c.fetchall()
    assert len(res) == 0

    c.execute("SELECT Sample_id FROM Sample WHERE Patient_id = '12'")
    sample_ids = c.fetchall()
    assert len(sample_ids) == 0
    conn.close()
    # os.remove("database.db")
