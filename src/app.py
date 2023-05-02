"""Command line tool for database management and data analysis."""
import sys
import os

path = os.path.abspath(".")
sys.path.append(path)

import argparse  # noqa: E402
from src.utils.check_db import link_to_database  # noqa: E402
from src.main import Patient, Sample  # noqa: E402
from src.analysis import perform_analysis  # noqa: E402


def main():
    """Command Lint Tool for DB and DA."""
    # link_to_database()
    parser = argparse.ArgumentParser(description="DB and DA Command Line Tool.")  # noqa
    parser.add_argument(
        "-f",
        "--function",
        type=str,
        choices=["db", "da"],
        help="use 'db' for database management, 'da' for data analysis",
    )
    parser.add_argument(
        "--db_function",
        type=str,
        choices=["add", "delete", "update"],
    )

    parser.add_argument("--db_level", type=str, choices=["patient", "sample"])

    args = parser.parse_args()
    function = args.function
    db_function = args.db_function
    level = args.db_level

    if function == "db":
        conn = link_to_database()
        if db_function == "add":
            if level == "patient":
                patient_id = input("Enter patient's ID: ")
                name = input("Enter patient's name: ")
                gender = input("Enter patient's gender (Female/Male/Other): ")
                dob_str = input("Enter patient's date of birth (YYYY-M-D): ")
                phone = int(input("Enter patient's phone number: "))
                email = input("Enter patient's email address: ")
                patient = Patient(conn, patient_id)
                patient.add_patient(name, gender, dob_str, phone, email)
            elif level == "sample":
                patient_id = input("Enter patient's ID: ")
                sample_id = input("Enter sample's ID: ")
                collection_date = input(
                    "Enter sample's collection date (YYYY-M-D): "
                )  # noqa
                cancer_type = input("Enter sample's cancer type: ")
                mutation_count = int(input("Enter sample's mutation count: "))
                chemotehrapy = input("If Chemotherapy (Yes/No): ")
                cas = float(input("Enter Cytolytic Activity Score: "))

                sample = Sample(conn, sample_id)
                sample.add_sample(
                    patient_id,
                    collection_date,
                    cancer_type,
                    mutation_count,
                    chemotehrapy,
                    cas,
                )

        elif db_function == "update":
            if level == "patient":
                patient_id = input("Enter patient's ID: ")
                name = input("Enter patient's name: ")
                gender = input("Enter patient's gender (Female/Male/Other): ")
                dob_str = input("Enter patient's date of birth (YYYY-M-D): ")
                phone = int(input("Enter patient's phone number: "))
                email = input("Enter patient's email address: ")
                patient = Patient(conn, patient_id)
                patient.update_patient(name, gender, dob_str, phone, email)

            elif level == "sample":
                patient_id = input("Enter patient's ID: ")
                sample_id = input("Enter sample's ID: ")
                collection_date = input(
                    "Enter sample's collection date (YYYY-M-D): "
                )  # noqa
                cancer_type = input("Enter sample's cancer type: ")
                mutation_count = int(input("Enter sample's mutation count: "))
                chemotehrapy = input("If Chemotherapy (Yes/No): ")
                cas = float(input("Enter Cytolytic Activity Score: "))

                sample = Sample(conn, sample_id)
                sample.update_sample(
                    patient_id,
                    collection_date,
                    cancer_type,
                    mutation_count,
                    chemotehrapy,
                    cas,
                )

        elif db_function == "delete":
            if level == "patient":
                patient_id = input("Enter patient's ID: ")
                patient = Patient(conn, patient_id)
                patient.delete_patient(patient_id)

            elif level == "sample":
                sample_id = input("Enter sample's ID: ")

                sample = Sample(conn, sample_id)
                sample.delete_sample(sample_id)

        conn.close()

    elif function == "da":
        perform_analysis()


if __name__ == "__main__":
    main()
