"""Upload data to db."""

import sqlite3
from datetime import datetime
from src.main import Patient, Sample
from src.utils.check_db import if_create_database

# Create a connection to the database
if_create_database()
conn = sqlite3.connect("database.db")

# Prompt the user to enter the patient's demographic data
patient_id = input("Enter patient's ID: ")
name = input("Enter patient's name: ")
gender = input("Enter patient's gender: ")
dob_str = input("Enter patient's date of birth (YYYY-MM-DD): ")
phone = int(input("Enter patient's phone number: "))
email = input("Enter patient's email address: ")

# Prompt the user to enter the patient's clinical data
patient_id = input("Enter patient's ID: ")
sample_id = input("Enter sample's ID: ")
collection_date = input("Enter sample's collection date: ")
cancer_type = input("Enter sample's cancer type: ")
mutation_count = int(input("Enter sample's mutation count: "))
chemotehrapy = input("If Chemotherapy (Yes/No): ")
cas = float(input("Enter Cytolytic Activity Score: "))

# Create a Patient object and add the patient to the database
patient = Patient(conn, patient_id)
patient.add_patient(name, gender, dob_str, phone, email)

sample = Sample(conn, sample_id)
sample.add_sample(
    patient_id, collection_date, cancer_type, mutation_count, chemotehrapy, cas
)

# Close the database connection
conn.close()
