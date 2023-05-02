"""Test analysis module."""

import pytest
import sqlite3
from typing import List, Tuple
from src.analysis import (
    ask_for_user_input,
    connect_db,
    select_analysis,
    # perform_analysis,
    find_unique_patients,
    find_unique_cancer_types,
    find_samples_in_cancer_type,
    find_age_distribution,
    find_samples_in_patient,
    find_samples_in_cancertype_patient,
)

# user_input = "/workspaces/Final__project/database.db"
# patient_results, sample_results = connect_db(user_input)

patient = [
    (
        "PO00",
        "John Doe",
        "Male",
        "1990-01-01 00:00:00",
        33,
        6174352673,
        "johndoe@gmail.com",
    ),
    (
        "RD34",
        "Alice Patel",
        "Female",
        "1989-08-23 00:00:00",
        33,
        8273647589,
        "alice@gmail.com",
    ),
    (
        "GK93",
        "Natalie Rodriguez",
        "Female",
        "1993-05-29 00:00:00",
        29,
        2734658393,
        "natalie@gmail.com",
    ),
]  # type: List[Tuple]

sample = [
    (
        "ace4357",
        "PO00",
        "2019-03-23 00:00:00",
        "Breast Invasive Ductal Carcinoma",
        37,
        "Yes",
        5.982,
    ),
    (
        "37rtbd",
        "PO00",
        "2021-01-28 00:00:00",
        "Breast Invasive Ductal Carcinoma",
        12,
        "Yes",
        7.27,
    ),
    (
        "23r8vb",
        "PO00",
        "2022-12-12 00:00:00",
        "Breast Invasive Carcinoma",
        8,
        "No",
        3.6,
    ),
    (
        "37fhvdf",
        "RD34",
        "2016-07-10 00:00:00",
        "Breast Invasive Ductal Carcinoma",
        55,
        "Yes",
        13.5,
    ),
    (
        "r640g",
        "RD34",
        "2018-03-31 00:00:00",
        "Breast Invasive Lobular Carcinoma",
        3,
        "No",
        18.9,
    ),
    (
        "er7t4t9",
        "GK93",
        "2023-01-21 00:00:00",
        "reast Invasive Ductal Carcinoma",
        34,
        "No",
        2.4,
    ),
]  # type: List[Tuple]


def test_ask_for_user_input(monkeypatch) -> None:
    """Test the ask_for_user_input function."""
    monkeypatch.setattr(
        "builtins.input", lambda _: "/workspaces/Final__project/database.db"
    )
    # Call the function being tested
    user_input = ask_for_user_input()
    # Check the result
    assert user_input == "/workspaces/Final__project/database.db"


def test_connect_db(monkeypatch) -> None:
    # Set up mock user input
    monkeypatch.setattr("builtins.input", lambda _: "database.db")
    user_input = ask_for_user_input()
    # Call the function being tested
    patient_results, sample_results = connect_db()
    assert patient_results == [
        (
            "PO00",
            "John Doe",
            "Male",
            "1990-01-01 00:00:00",
            33,
            6174352673,
            "johndoe@gmail.com",
        ),
        (
            "RD34",
            "Alice Patel",
            "Female",
            "1989-08-23 00:00:00",
            33,
            8273647589,
            "alice@gmail.com",
        ),
        (
            "GK93",
            "Natalie Rodriguez",
            "Female",
            "1993-05-29 00:00:00",
            29,
            2734658393,
            "natalie@gmail.com",
        ),
    ]
    assert sample_results == [
        (
            "ace4357",
            "PO00",
            "2019-03-23 00:00:00",
            "Breast Invasive Ductal Carcinoma",
            37,
            "Yes",
            5.982,
        ),
        (
            "37rtbd",
            "PO00",
            "2021-01-28 00:00:00",
            "Breast Invasive Ductal Carcinoma",
            12,
            "Yes",
            7.27,
        ),
        (
            "23r8vb",
            "PO00",
            "2022-12-12 00:00:00",
            "Breast Invasive Carcinoma",
            8,
            "No",
            3.6,
        ),
        (
            "37fhvdf",
            "RD34",
            "2016-07-10 00:00:00",
            "Breast Invasive Ductal Carcinoma",
            55,
            "Yes",
            13.5,
        ),
        (
            "r640g",
            "RD34",
            "2018-03-31 00:00:00",
            "Breast Invasive Lobular Carcinoma",
            3,
            "No",
            18.9,
        ),
        (
            "er7t4t9",
            "GK93",
            "2023-01-21 00:00:00",
            "reast Invasive Ductal Carcinoma",
            34,
            "No",
            2.4,
        ),
    ]


def test_select_anlaysis(monkeypatch):
    """Test the select_analysis function."""
    monkeypatch.setattr("builtins.input", lambda _: "3")
    # Call the function being tested
    value = select_analysis()
    # Check the result
    assert value == "3"


def test_find_unique_patients() -> None:
    """Test find_unique_patients function."""

    assert find_unique_patients(patient) == 3


def test_find_unique_cancer_types() -> None:
    """Test find_unique_cancer_types function."""
    assert find_unique_cancer_types(sample) == 4


def test_find_samples_in_cancer_type() -> None:
    """Test find_samples_in_cancer_type function."""
    assert find_samples_in_cancer_type(sample) == {
        "Breast Invasive Carcinoma": 1,
        "Breast Invasive Ductal Carcinoma": 3,
        "Breast Invasive Lobular Carcinoma": 1,
        "reast Invasive Ductal Carcinoma": 1,
    }


def test_find_age_distribution() -> None:
    """Test find_age_distribution function."""
    assert find_age_distribution(patient) == {33: 2, 29: 1}


def test_find_samples_in_patient() -> None:
    """Test find_samples_in_patient function."""
    assert find_samples_in_patient(sample) == {"PO00": 3, "RD34": 2, "GK93": 1}


def test_find_samples_in_cancertype_patient() -> None:
    """Test find_samples_in_cancertype_patient function."""
    assert find_samples_in_cancertype_patient(sample) == {
        "PO00": {
            "Breast Invasive Ductal Carcinoma": 2,
            "Breast Invasive Carcinoma": 1,
        },
        "RD34": {
            "Breast Invasive Ductal Carcinoma": 1,
            "Breast Invasive Lobular Carcinoma": 1,
        },
        "GK93": {"reast Invasive Ductal Carcinoma": 1},
    }
