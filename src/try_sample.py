"""Upload sample data to db."""

import sqlite3
from src.main import Sample
from src.utils.check_db import if_create_database

# Create a connection to the database
if_create_database()
conn = sqlite3.connect("database.db")

# Prompt the user to enter the patient's clinical data
patient_id = input("Enter patient's ID: ")
sample_id = input("Enter sample's ID: ")
collection_date = input("Enter sample's collection date (YYYY-M-D): ")
cancer_type = input("Enter sample's cancer type: ")
mutation_count = int(input("Enter sample's mutation count: "))
chemotehrapy = input("If Chemotherapy (Yes/No): ")
cas = float(input("Enter Cytolytic Activity Score: "))

sample = Sample(conn, sample_id)
sample.add_sample(
    patient_id, collection_date, cancer_type, mutation_count, chemotehrapy, cas
)

# Close the database connection
conn.close()
