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
        c.execute(
            """CREATE TABLE Sample (Sample_id TEXT PRIMARY KEY, \
                Patient_id TEXT NOT NULL, Collection_date DATE NOT NULL, \
                    Cancer_type TEXT NOT NULL, Mutation_count INTEGER, \
                        Chemotherapy TEXT, Cytolytic_activity_score REAL, FOREIGN KEY \
                            (patient_id) REFERENCES Patient(patient_id)) """
        )
        conn.commit()
        conn.close()
