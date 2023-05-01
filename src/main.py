"""Main Python Module."""

import sqlite3
from datetime import datetime

conn = sqlite3.connect("mydatabase.db")
conn.execute(
    """
CREATE TABLE Patient (
    patient_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    gender TEXT NOT NULL,
    dob DATE NOT NULL,
    age INTEGER,
    phone TEXT,
    email TEXT
)
"""
)

conn.execute(
    """
CREATE TABLE Sample (
    sample_id INTEGER PRIMARY KEY,
    patient_id INTEGER NOT NULL,
    collection_date DATE NOT NULL,
    type TEXT NOT NULL,
    mutation_count INTEGER,
    chemotherapy TEXT,
    CAS INTEGER,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
)
"""
)


class Patient:
    def __init__(
        self,
        name: str,
        gender: str,
        dob: str,
        age: int,
        phone: int,
        email: str,
        patient_id: str,
    ):
        self.name = name
        self.gender = gender
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()
        self.age = age
        self.phone = phone
        self.email = email
        self.patient_id = patient_id

        # Validate age input
        if age is not None:
            try:
                age_int = int(age)
                if age_int < 0:
                    print("Please enter a valid age (greater than or equal to 0)")
                else:
                    tod = datetime.today()
                    calculated_age = (
                        tod.year
                        - self.dob.year
                        - ((tod.month, tod.day) < (self.dob.month, self.dob.day))
                    )
                    if age_int != calculated_age:
                        print("Please enter the correct age")
            except ValueError:
                print("Please enter a valid age (an integer)")

    def add_to_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            # check if patient_id already exists
            c.execute(
                "SELECT COUNT(*) FROM Patient WHERE patient_id = ?", (self.patient_id,)
            )
            count = c.fetchone()[0]
            if count > 0:
                print(
                    f"Patient with ID {self.patient_id} already exists in the database."
                )
                return
            # insert new patient record
            c.execute(
                "INSERT INTO Patient (patient_id, name, gender, dob, age, phone, email) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    self.patient_id,
                    self.name,
                    self.gender,
                    self.dob,
                    self.age,
                    self.phone,
                    self.email,
                ),
            )
            conn.commit()

    def delete_from_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM Patient WHERE patient_id = ?", (self.patient_id,))
            c.execute("DELETE FROM Sample WHERE patient_id = ?", (self.patient_id,))
            conn.commit()

    def update_in_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE Patient SET name = ?, gender = ?, dob = ?, age = ?, phone = ?, email = ? WHERE patient_id = ?",
                (
                    self.name,
                    self.gender,
                    self.dob,
                    self.age,
                    self.phone,
                    self.email,
                    self.patient_id,
                ),
            )
            conn.commit()


class Sample:
    def __init__(
        self, patient_id, type, collection_date, mutation_count, chemotherapy, CAS
    ):
        self.patient_id = patient_id
        self.type = type
        self.collection_date = collection_date
        self.mutation_count = mutation_count
        self.chemotherapy = chemotherapy
        self.CAS = CAS

    def add_to_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()

            # Check if patient_id exists in Patient table
            c.execute(
                "SELECT COUNT(*) FROM Patient WHERE patient_id = ?", (self.patient_id,)
            )
            if c.fetchone()[0] == 0:
                raise ValueError(
                    "Patient with patient_id {} does not exist in database".format(
                        self.patient_id
                    )
                )

            # Insert row into Sample table
            c.execute(
                "INSERT INTO Sample (patient_id, type, collection_date, mutation_count, chemotherapy, CAS) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    self.patient_id,
                    self.type,
                    self.collection_date,
                    self.mutation_count,
                    self.chemotherapy,
                    self.CAS,
                ),
            )
            conn.commit()
            self.sample_id = c.lastrowid

    def delete_from_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM Sample WHERE sample_id = ?", (self.sample_id,))
            conn.commit()

            # check if patient has any other samples in the database
            c.execute(
                "SELECT COUNT(*) FROM Sample WHERE patient_id = ?", (self.patient_id,)
            )
            num_samples = c.fetchone()[0]

            # if patient has no other samples, delete the patient record
            if num_samples == 0:
                c.execute(
                    "DELETE FROM Patient WHERE patient_id = ?", (self.patient_id,)
                )
                conn.commit()

    def update_in_db(self, db_path):
        with sqlite3.connect(db_path) as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE Sample SET patient_id = ?, type = ?, collection_date = ?, mutation_count = ?, chemotherapy = ?, CAS = ? WHERE sample_id = ?",
                (
                    self.patient_id,
                    self.type,
                    self.collection_date,
                    self.mutation_count,
                    self.chemotherapy,
                    self.CAS,
                ),
            )
            conn.commit()


name = input("Enter patient name: ")
patient_id = input("Enter patient ID: ")
gender = input("Enter patient biological gender (e.g. Male/Female/Other): ")
dob = input("Enter patient date of birth (YYYY-MM-DD): ")
age = input("Enter patient age (or leave blank if unknown): ")
phone = input("Enter patient phone number (e.g. XXX-XXX-XXXX): ")
email = input("Enter patient email address (or leave blank if unknown): ")
p = Patient(name, gender, dob, age, phone, email, patient_id)
p.add_to_db("mydatabase.db")

patient_id = input("Enter patient ID: ")
type = input(
    "Enter cancer type (e.g. Breast Invasive Ductal Carcinoma/Breast Invasive Carcinoma/Breast Invasive Lobular Carcinoma): "
)
collection_date = input("Enter collection date (YYYY-MM-DD): ")
mutation_count = input("Enter mutation count (or leave blank if unknown): ")
chemotherapy = input("Enter chemotherapy (if applicable, otherwise leave blank): ")
CAS = input("Enter Cytolytic Activity Score (if applicable, otherwise leave blank): ")
s = Sample(patient_id, type, collection_date, mutation_count, chemotherapy, CAS)
s.add_to_db("mydatabase.db")
