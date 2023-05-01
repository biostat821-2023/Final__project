"""Main Python Module."""

import sqlite3
from datetime import datetime

# create connection object
conn = sqlite3.connect("mydatabase.db")

# create tables if they don't exist
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
    cancer_type TEXT NOT NULL,
    mutation_count INTEGER,
    chemotherapy TEXT,
    CAS INTEGER,
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
)
"""
)


class Patient:
    """Class for patient's demographic record."""

    def __init__(
        self,
        name: str,
        gender: str,
        dob: str,
        age: int,
        phone: int,
        email: str,
        patient_id: str,
        conn: sqlite3.Connection,
    ) -> None:
        """Initialize Patient obejct."""
        self.name = name
        self.gender = gender
        self.birthdate = datetime.strptime(dob, "%Y-%m-%d").date()
        self.age = age
        self.phone = phone
        self.email = email
        self.p_id = patient_id
        self.conn = conn

        # Validate age input
        if age is not None:
            try:
                age_int = int(age)
                if age_int < 0:
                    print("Please enter a valid age (non-negative)")
                else:
                    tod = datetime.today()
                    calculated_age = (
                        tod.year
                        - self.birthdate.year
                        - (
                            (tod.month, tod.day)
                            < (self.birthdate.month, self.birthdate.day)
                        )
                    )
                    if age_int != calculated_age:
                        print("Please enter the correct age")
            except ValueError:
                print("Please enter a valid age (an integer)")

    def add_to_db(self) -> None:
        """Add patient demographic record to table."""
        c = self.conn.cursor()
        # check if patient_id already exists
        c.execute(
            "SELECT COUNT(*) FROM Patient \
                WHERE patient_id = ?",
            (self.p_id,),
        )
        count = c.fetchone()[0]
        if count > 0:
            print(f"Patient with ID {self.p_id} already exists.")
            return
        # insert new patient record
        c.execute(
            "INSERT INTO Patient "
            "(patient_id, name, gender, dob, age, phone, email) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                self.p_id,
                self.name,
                self.gender,
                self.birthdate,
                self.age,
                self.phone,
                self.email,
            ),
        )
        self.conn.commit()

    def delete_from_db(self) -> None:
        """Delete patient's demographic record from table."""
        c = self.conn.cursor()
        c = conn.cursor()
        c.execute("DELETE FROM Patient WHERE patient_id = ?", (self.p_id,))
        c.execute("DELETE FROM Sample WHERE patient_id = ?", (self.p_id,))
        self.conn.commit()

    def update_in_db(self) -> None:
        """Update patient's demographic record from table."""
        c = self.conn.cursor()
        c.execute(
            "UPDATE Patient SET name = ?, gender = ?, "
            "dob = ?, age = ?, phone = ?, email = ? "
            "WHERE patient_id = ?",
            (
                self.name,
                self.gender,
                self.birthdate,
                self.age,
                self.phone,
                self.email,
                self.p_id,
            ),
        )
        self.conn.commit()


class Sample:
    """Class for patient's clinical record."""

    def __init__(
        self,
        patient_id: str,
        cancer_type: str,
        collection_date: str,
        mutation_count: int,
        chemotherapy: str,
        CAS: int,
        conn: sqlite3.Connection,
        sample_id=None,
    ) -> None:
        """Initialize Sample object."""
        self.p_id = patient_id
        self.cancer_type = cancer_type
        self.collection_date = collection_date
        self.mutation_count = mutation_count
        self.chemotherapy = chemotherapy
        self.CAS = CAS
        self.conn = conn
        self.sample_id = sample_id

    def add_to_db(self) -> None:
        """Add patinet's clinical record to table."""
        c = conn.cursor()

        # Check if patient_id exists in Patient table
        c.execute(
            "SELECT COUNT(*) FROM Patient \
            WHERE patient_id = ?",
            (self.p_id,),
        )
        if c.fetchone()[0] == 0:
            raise ValueError(
                "Patient with patient_id {} does "
                "not exist in database".format(self.p_id)
            )

        # Insert row into Sample table
        c.execute(
            "INSERT INTO Sample (patient_id, cancer_type, "
            "collection_date, mutation_count, chemotherapy, CAS) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (
                self.p_id,
                self.cancer_type,
                self.collection_date,
                self.mutation_count,
                self.chemotherapy,
                self.CAS,
            ),
        )
        self.conn.commit()
        self.sample_id = c.lastrowid

    def delete_from_db(self) -> None:
        """Delete patient's clinical record from table."""
        c = self.conn.cursor()
        c.execute(
            "SELECT patient_id FROM Sample WHERE sample_id = ?",
            (self.sample_id,),
        )
        patient_id = c.fetchone()[0]
        c.execute(
            "DELETE FROM Sample \
                WHERE sample_id = ?",
            (self.sample_id,),
        )
        self.conn.commit()

        # check if patient has any other samples in the database
        c.execute(
            "SELECT COUNT(*) FROM Sample " "WHERE patient_id = ?",
            (patient_id,),
        )
        num_samples = c.fetchone()[0]

        # if patient has no other samples, delete the patient record
        if num_samples == 0:
            c.execute(
                "DELETE FROM Patient \
                WHERE patient_id = ?",
                (self.p_id,),
            )
            self.conn.commit()

    def update_in_db(self) -> None:
        """Update patient's clinical record from table."""
        c = self.conn.cursor()
        c.execute(
            "UPDATE Sample SET patient_id = ?, cancer_type = ?, "
            "collection_date = ?, mutation_count = ?, "
            "chemotherapy = ?, CAS = ? WHERE sample_id = ?",
            (
                self.p_id,
                self.cancer_type,
                self.collection_date,
                self.mutation_count,
                self.chemotherapy,
                self.CAS,
            ),
        )
        self.conn.commit()
