"""Crude Analysis on Clinical Information."""

import sqlite3
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # type: ignore
from dataclasses import dataclass
from typing import List, Tuple, Dict
from datetime import datetime
from src.main import Patient, Sample


def ask_for_user_input() -> str:
    """Ask for user input to determine the database to connect to."""
    while True:
        user_input = input(
            f"Enter the name of the database to connect to" f" or type 'exit' to quit: "
        )
        if user_input == "exit":
            exit()
        if os.path.exists(user_input):
            return user_input
        print(f"Database file {user_input} not found.")
        print(f"Please enter a valid file name.")


def connect_db() -> Tuple[List[Tuple], List[Tuple]]:
    """Connect to the database."""
    user_input = ask_for_user_input()
    conn = sqlite3.connect(user_input)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patient;")
    patient_results = cur.fetchall()
    cur.execute("SELECT * FROM Sample;")
    sample_results = cur.fetchall()
    return patient_results, sample_results


# # For easy testing
# patient_results, sample_results = connect_db()
# print(patient_results)
# print(sample_results)


def select_analysis() -> str:
    """Select the analysis to perform."""
    user_input = input(
        f"Please enter the number of the analysis you want to perform: "
        f"\n1. Find the unique number of patients in the database"
        f"\n2. Find the unique number of cancer types in the database"
        f"\n3. Find the number of samples in each cancer type"
        f"\n4. Find the age distribution of the patients"
        f"\n5. Find the number of samples for each patient"
        f"\n6. Fidn the number of samples for each cancer type for patient"
    )
    return user_input


def perform_analysis() -> None:
    """Perform the analysis."""
    value = select_analysis()
    patient_results, sample_results = connect_db()
    if value == "1":
        find_unique_patients(patient_results)
    elif value == "2":
        find_unique_cancer_types(sample_results)
    elif value == "3":
        find_samples_in_cancer_type(sample_results)
    elif value == "4":
        find_age_distribution(patient_results)
    elif value == "5":
        find_samples_in_patient(sample_results)
    elif value == "6":
        find_samples_in_cancertype_patient(sample_results)
    else:
        print("Invalid input. Please try again.")


# Find the unique number of patients in the database
def find_unique_patients(patients: List[Tuple]) -> int:
    """Find the unique number of patients in the database."""
    unique_patients = set()
    for patient in patients:
        unique_patients.add(patient[0])
    return len(unique_patients)


# Find the unique number of cancer types in the database
def find_unique_cancer_types(samples: List[Tuple]) -> int:
    """Find the unique number of cancer types in the database."""
    unique_cancer_types = set()
    for sample in samples:
        unique_cancer_types.add(sample[3])
    return len(unique_cancer_types)


# Find the number of samples in each cancer type
def find_samples_in_cancer_type(samples: List[Tuple]) -> dict:
    """Find the number of samples in each cancer type."""
    cancer_type_dict = {}
    for sample in samples:
        if sample[3] not in cancer_type_dict:
            cancer_type_dict[sample[3]] = 1
        else:
            cancer_type_dict[sample[3]] += 1
    return cancer_type_dict


# Find the age distribution of the patients
def find_age_distribution(patients: List[Tuple]) -> dict:
    """Find the age distribution of the patients."""
    age_dict = {}
    for patient in patients:
        if patient[4] not in age_dict:
            age_dict[patient[4]] = 1
        else:
            age_dict[patient[4]] += 1
    return age_dict


# Visualize the number of samples in each cancer type
def plot_samples_in_cancer_type(samples: List[Tuple]) -> None:
    """Plot the number of samples in each cancer type."""
    cancer_type = [sample[3] for sample in samples]
    plt.hist(cancer_type)
    plt.xlabel("Cancer Type")
    plt.ylabel("Number of Samples")
    plt.title("Number of Samples in Each Cancer Type")
    plt.savefig("../cancer_type.png")
    plt.show()


# Visualize the age distribution of the patients
def plot_age_distribution(patients: List[Tuple]) -> None:
    """Plot the age distribution of the patients."""
    age = [patient[4] for patient in patients]
    plt.hist(age, bins=20)
    plt.xlabel("Age")
    plt.ylabel("Number of Patients")
    plt.title("Age Distribution of Patients")
    plt.show()


# Find the number of samples in each patient
def find_samples_in_patient(samples: List[Tuple]) -> Dict[str, int]:
    """Find the number of samples in each patient."""
    patient_dict = {}  # type: Dict[str, int]
    for sample in samples:
        if sample[1] not in patient_dict:
            patient_dict[sample[1]] = 1
        else:
            patient_dict[sample[1]] += 1
    return patient_dict


# Find the number of samples in each cancer type of each patient
def find_samples_in_cancertype_patient(samples: List[Tuple]) -> Dict[str, int]:
    """Find the number of samples in each cancer type of each patient."""
    patient_cancer_type_dict = {}  # type: ignore
    for sample in samples:
        if sample[1] not in patient_cancer_type_dict:
            patient_cancer_type_dict[sample[1]] = {}  # type: ignore
        if sample[3] not in patient_cancer_type_dict[sample[1]]:
            patient_cancer_type_dict[sample[1]][sample[3]] = 1
        else:
            patient_cancer_type_dict[sample[1]][sample[3]] += 1
    return patient_cancer_type_dict
