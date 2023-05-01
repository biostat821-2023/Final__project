"""Helper Function Module."""

import sqlite3
import os


def if_create_database():
    """Create database if it doesn't exist."""
    if not os.path.exists("database.db"):
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute(
            """CREATE TABLE Patient
                     (Patient_id TEXT, Name TEXT, Gender TEXT, \
                        DateofBirth DATE, Age INTEGER, Phone INTEGER, \
                            Email TEXT, PRIMARY KEY (patient_id))"""
        )
        conn.execute(
            """CREATE TABLE Sample (Sample_id INTEGER PRIMARY KEY, \
                Patient_id INTEGER NOT NULL, Collection_date DATE NOT NULL, \
                    Cancer_type TEXT NOT NULL, Mutation_count INTEGER, \
                        Chemotherapy TEXT, CAS INTEGER, FOREIGN KEY \
                            (patient_id) REFERENCES Patient(patient_id)) """
        )
        conn.commit()
        conn.close()
