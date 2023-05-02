"""Upload patient data to db."""

import sqlite3
from src.main import Patient
from src.utils.check_db import if_create_database

# Create a connection to the database
if_create_database()
conn = sqlite3.connect("database.db")

# Prompt the user to enter the patient's demographic data
patient_id = input("Enter patient's ID: ")
name = input("Enter patient's name: ")
gender = input("Enter patient's gender (Female/Male/Other): ")
dob_str = input("Enter patient's date of birth (YYYY-M-D): ")
phone = int(input("Enter patient's phone number: "))
email = input("Enter patient's email address: ")


# Create a Patient object and add the patient to the database
patient = Patient(conn, patient_id)
patient.add_patient(name, gender, dob_str, phone, email)

# Close the database connection
conn.close()
