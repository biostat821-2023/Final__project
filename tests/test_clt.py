"""Test CLT."""
import monkeypatch
from src.app import main
import sqlite3
import os


def test_add_patient(monkeypatch):
    args = ["-f", "db", "--db_function", "add", "--db_level patient"]
    main(args)
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * from Patient where Patient_id = '123'")
    inputs = ["12", "Test Name", "1980-1-1", 123, "test@gmail.com"]
    for input in inputs:
        monkeypatch.setattr("builtins.input", lambda _: input)
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
