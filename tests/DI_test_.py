"""Test Module."""

import os
import sys
import unittest
import sqlite3
from datetime import datetime
from src.main import Patient, Sample


class TestPatient(unittest.TestCase):
    """Class for testing Patient's functions."""

    def Setup(self):
        """Set up function."""
        self.conn = sqlite3.connect(":memory:")
        self.patient = Patient(self.conn, "ABC")
        self.patient.add_patient(
            "John Doe", "Male", "1980-1-1", 1234567890, "johndoe@example.com"
        )

    def test_add_patient(self):
        """Test if patient's record is added."""
        c = self.conn.cursor()
        c.execute("SELECT * from Patient where Patient_id = 'ABC'")
        result = c.fetchall()
        self.assertEqual(result[0], "ABC")
        self.assertEqual(result[1], "John Doe")
        self.assertEqual(result[2], "Male")
        self.assertEqual(result[3], datetime(1980, 1, 1, 0, 0))
        self.assertEqual(result[4], 43)
        self.assertEqual(result[5], 1234567890)
        self.assertEqual(result[6], "johndoe@example.com")

    def test_delete_patient(self):
        """Test if patient's record is deleted."""
        # Check if table Patient is empty
        self.patient.delete_patient("ABC")
        c = self.conn.cursor()
        c.execute("SELECT * FROM Patient WHERE Patient_id = 'ABC'")
        result = c.fetchone()
        self.assertIsNone(result)

        # Check if table Sample is empty
        c = self.conn.cursor()
        c.execute("SELECT Sample_id FROM Sample WHERE Patient_id = 'ABC'")
        sample_id = c.fetchall()[0]
        c.execute(
            "SELECT * FROM Sample WHERE Sample_id = ?",
            (sample_id,),
        )
        result_s = c.fetchone()
        self.assertIsNone(result_s)

    def test_update_patient(self):
        """Test if patient's record is updated."""
        self.patient.update_patient(
            "Jason Wong", "Male", "1980-1-1", 1234567890, "jason@example.com"
        )
        c = self.conn.cursor()
        c.execute("SELECT * FROM Patient WHERE Patient_id = 'ABC'")
        result = c.fetchall()
        self.assertEqual(result[0], "ABC")
        self.assertEqual(result[1], "Jason Wong")
        self.assertEqual(result[2], "Male")
        self.assertEqual(result[3], datetime(1980, 1, 1, 0, 0))
        self.assertEqual(result[4], 43)
        self.assertEqual(result[5], 1234567890)
        self.assertEqual(result[6], "jason@example.com")


class TestSample(unittest.TestCase):
    """Class for testing Sample's functions."""

    def Setup(self):
        """Set up function."""
        self.conn = sqlite3.connect(":memory:")
        self.sample = Sample(self.conn, "8ehciud")
        self.sample.add_sample(
            "ABC", "2019-3-30", "Breast Invasive Carcinoma", 12, "Yes", 12.5
        )

    def test_add_sample(self):
        """Test if sample's record is added."""
        c = self.conn.cursor()
        c.execute("SELECT * from Patient where Patient_id = 'ABC'")
        result = c.fetchall()
        self.assertEqual(result[0], "8ehciud")
        self.assertEqual(result[1], "ABC")
        self.assertEqual(result[2], datetime(2019, 3, 30, 0, 0))
        self.assertEqual(result[3], "Breast Invasive Carcinoma")
        self.assertEqual(result[4], 12)
        self.assertEqual(result[5], "Yes")
        self.assertEqual(result[6], 12.5)

    def test_delete_sample(self):
        """Test if sample's record is deleted."""
        # Check if table Sample is empty
        self.sample.delete_sample("8ehciud")
        c = self.conn.cursor()
        c.execute("SELECT * FROM Sample WHERE Sample_id = '8ehciud'")
        result = c.fetchone()
        self.assertIsNone(result)

        # Check if table Patient is empty
        c.execute(
            "SELECT Patient_id FROM Sample \
                WHERE Sample_id = 8ehciud"
        )
        patient_id = c.fetchone()[0]
        c.execute(
            "SELECT * FROM Patient WHERE Patient_id = ?",
            (patient_id,),
        )
        result_p = c.fetchone()
        self.assertIsNone(result_p)

    def test_update_sample(self):
        """Test if sample's record is updated."""
        self.sample.update_sample(
            "ABC", "2020-4-29", "Breast Invasive Carcinoma", 6, "No", 23.3
        )
        c = self.conn.cursor()
        c.execute("SELECT * FROM Sample WHERE Sample_id = '8ehciud'")
        result = c.fetchall()
        self.assertEqual(result[0], "8ehciud")
        self.assertEqual(result[1], "ABC")
        self.assertEqual(result[2], datetime(2020, 4, 29, 0, 0))
        self.assertEqual(result[3], "Breast Invasive Carcinoma")
        self.assertEqual(result[4], 6)
        self.assertEqual(result[5], "No")
        self.assertEqual(result[6], 23.3)
