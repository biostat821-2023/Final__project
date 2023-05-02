"""Test analysis module."""

import pytest

from src.analysis import (
    ask_for_user_input,
    connect_db,
    find_unique_patients,
    find_unique_cancer_types,
    find_samples_in_cancer_type,
    find_age_distribution,
    find_unique_patients,
    find_unique_cancer_types,
)

user_input = "/workspaces/Final__project/database.db"


def test_connect_db() -> None:
    """Test connect_db function."""
    patient_results, sample_results = connect_db(user_input)
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


patient_results, sample_results = connect_db(user_input)


def test_find_unique_patients() -> None:
    """Test find_unique_patients function."""
    assert find_unique_patients(patient_results) == 3


def test_find_unique_cancer_types() -> None:
    """Test find_unique_cancer_types function."""
    assert find_unique_cancer_types(sample_results) == 4


def test_find_samples_in_cancer_type() -> None:
    """Test find_samples_in_cancer_type function."""
    assert find_samples_in_cancer_type(sample_results) == {
        "Breast Invasive Ductal Carcinoma": 3,
        "Breast Invasive Carcinoma": 1,
        "Breast Invasive Lobular Carcinoma": 1,
        "reast Invasive Ductal Carcinoma": 1,
    }


def test_find_age_distribution() -> None:
    """Test find_age_distribution function."""
    assert find_age_distribution(patient_results) == {33: 2, 29: 1}
