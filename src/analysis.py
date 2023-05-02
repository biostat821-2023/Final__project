"""Crude Analysis on Clinical Information."""

import sqlite3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List
from datetime import datetime
from main import Patient, Sample


# Connect to database
conn = sqlite3.connect("/workspaces/Final__project/database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM Patient;")
patient_results = cur.fetchall()
cur.execute("SELECT * FROM Sample;")
sample_results = cur.fetchall()

print(patient_results)
print(sample_results)

# Analyze global information of the dataset
#     - Number of patients
#     - Number of cancer types
#     - Number of samples in each cancer type
#     - Age distribution


# Find the unique number of patients in the database
def find_unique_patients(patients: List[Patient]) -> int:
    """Find the unique number of patients in the database."""
    unique_patients = set()
    for patient in patients:
        unique_patients.add(patient[0])
    return len(unique_patients)

# Find the unique number of cancer types in the database
def find_unique_cancer_types(samples: List[Sample]) -> int:
    """Find the unique number of cancer types in the database."""
    unique_cancer_types = set()
    for sample in samples:
        unique_cancer_types.add(sample[3])
    return len(unique_cancer_types)

print(f"Total number of patients in our database is: {find_unique_patients(patient_results)}.")
print(f"Total number of samples in our database is: {len(sample_results)}.")
print(f"Total number of cancer types in our database is: {find_unique_cancer_types(sample_results)}.")

# Find the number of samples in each cancer type
def find_samples_in_cancer_type(samples: List[Sample]) -> dict:
    """Find the number of samples in each cancer type."""
    cancer_type_dict = {}
    for sample in samples:
        if sample[3] not in cancer_type_dict:
            cancer_type_dict[sample[3]] = 1
        else:
            cancer_type_dict[sample[3]] += 1
    return cancer_type_dict

print(f"Number of samples in each cancer type is: {find_samples_in_cancer_type(sample_results)}.")

# Find the age distribution of the patients
def find_age_distribution(patients: List[Patient]) -> dict:
    """Find the age distribution of the patients."""
    age_dict = {}
    for patient in patients:
        if patient[4] not in age_dict:
            age_dict[patient[4]] = 1
        else:
            age_dict[patient[4]] += 1
    return age_dict

print(f"Age distribution of the patients is: {find_age_distribution(patient_results)}.")

# Visualize the number of samples in each cancer type
def plot_samples_in_cancer_type(samples: List[Sample]) -> None:
    """Plot the number of samples in each cancer type."""
    cancer_type = [sample[3] for sample in samples]
    plt.hist(cancer_type)
    plt.xlabel("Cancer Type")
    plt.ylabel("Number of Samples")
    plt.title("Number of Samples in Each Cancer Type")
    plt.savefig("../cancer_type.png")
    plt.show()
  
plot_samples_in_cancer_type(sample_results)

# Visualize the age distribution of the patients
def plot_age_distribution(patients: List[Patient]) -> None:
    """Plot the age distribution of the patients."""
    age = [patient[4] for patient in patients]
    plt.hist(age, bins=20)
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    plt.title("Age Distribution of Patients")
    plt.show()

plot_age_distribution(patient_results)

# Analyze patient information
#     - Number of samples in each patient
#     - Number of samples in each cancer type of each patient

