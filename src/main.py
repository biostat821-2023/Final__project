"""Main Python Module."""

import sqlite3
from datetime import datetime
from src.utils.utils import Record
from src.utils.check_db import if_create_database


class Patient(Record):
    """Class for patient's clinical record."""

    def __init__(self, conn: sqlite3.Connection, patient_id: str) -> None:
        """Initialize Sample object."""
        super().__init__(conn, "Patient")
        self.p_id = patient_id
        if_create_database()

    def add_patient(
        self,
        name: str,
        gender: str,
        dob_str: str,
        phone: int,
        email: str,
    ) -> None:
        """Add patient's demographic record to the database."""
        tod = datetime.today()
        dob = datetime.strptime(
            dob_str,
            "%Y-%m-%d",
        )
        calculated_age = (
            tod.year - dob.year - ((tod.month, tod.day) < (dob.month, dob.day))
        )
        record_data = {
            "Patient_id": self.p_id,
            "Name": name,
            "Gender": gender,
            "DateofBorth": dob,
            "Age": calculated_age,
            "Phone": phone,
            "Email": email,
        }
        self.add_to_db(record_data, "Patient_id")

    def delete_patient(self, patient_id: str):
        """Delete patient's demo and clinical record from the database."""
        c = self.conn.cursor()
        # Find the sample id and get those clinical records
        c.execute(
            "SELECT Sample_id FROM Sample \
                WHERE Patient_id = ?",
            (patient_id,),
        )
        sample_ids = c.fetchall()

        # Delete all the samples associated with the patient in Sample table
        for sample_id in sample_ids:
            Sample(self.conn, sample_id[0]).delete_sample(sample_id[0])

        # Delete the patient's demographic record in Patient table
        self.delete_from_db(patient_id, "Patient_id")

    def update_patient(
        self,
        name: str,
        gender: str,
        dob_str: str,
        phone: int,
        email: str,
    ) -> None:
        """Update patient's demographic record in the database."""
        tod = datetime.today()
        dob = datetime.strptime(
            dob_str,
            "%Y-%m-%d",
        )
        calculated_age = (
            tod.year - dob.year - ((tod.month, tod.day) < (dob.month, dob.day))
        )
        record_data = {
            "Patient_id": self.p_id,
            "Name": name,
            "Gender": gender,
            "DateofBirth": dob,
            "Age": calculated_age,
            "Phone": phone,
            "Email": email,
        }
        self.update_in_db(record_data, "Patient_id")


class Sample(Record):
    """Class for sample record."""

    def __init__(self, conn: sqlite3.Connection, sample_id: str) -> None:
        """Initialize Sample object."""
        super().__init__(conn, "Sample")
        self.s_id = sample_id
        if_create_database()

    def add_sample(
        self,
        patient_id: str,
        collection_date_str: str,
        cancer_type: str,
        mutation_count: int,
        chemotherapy: str,
        cas: float,
    ) -> None:
        """Add sample to the database."""
        collection_date = datetime.strptime(
            collection_date_str,
            "%Y-%m-%d",
        )
        record_data = {
            "Patient_id": patient_id,
            "Sample_id": self.s_id,
            "Collection_date": collection_date,
            "Cancer_type": cancer_type,
            "Mutation_count": mutation_count,
            "Chemotherapy": chemotherapy,
            "Cytolytic_activity_score": cas,
        }
        self.add_to_db(record_data, "Sample_id")

    def delete_sample(self, sample_id: str) -> None:
        """Delete sample from the database."""
        c = self.conn.cursor()

        # get the patient id associated with sample id
        c.execute(
            "SELECT Patient_id FROM Sample \
                WHERE Sample_id = ?",
            (sample_id,),
        )
        patient_id = c.fetchone()[0]
        self.delete_from_db(sample_id, "Sample_id")
        # Check if patient has any remaining samples
        c = self.conn.cursor()
        c.execute(
            "SELECT COUNT(*) FROM Sample \
            WHERE Patient_id = ?",
            (patient_id,),
        )
        count = c.fetchone()[0]

        # If the patient has no remaining samples, delete the patient's record
        if count == 0:
            Patient(self.conn, patient_id).delete_patient(patient_id)

    def update_sample(
        self,
        patient_id: str,
        collection_date_str: str,
        cancer_type: str,
        mutation_count: int,
        chemotherapy: str,
        cas: float,
    ) -> None:
        """Update sample in the database."""
        collection_date = datetime.strptime(
            collection_date_str,
            "%Y-%m-%d",
        )
        record_data = {
            "Patient_id": patient_id,
            "Sample_id": self.s_id,
            "Collection_date": collection_date,
            "Cancer_type": cancer_type,
            "Mutation_count": mutation_count,
            "Chemotherapy": chemotherapy,
            "Cytolytic_activity_score": cas,
        }
        self.update_in_db(record_data, "Sample_id")
