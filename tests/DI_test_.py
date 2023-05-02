"""Test Module."""
import sqlite3
from src.main import Patient, Sample

conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute(
    """CREATE TABLE Patient
            (Patient_id TEXT, Name TEXT, Gender TEXT, \
            DateofBirth DATE, Age INTEGER, Phone INTEGER, \
            Email TEXT, PRIMARY KEY (patient_id))"""
)
c.execute(
    """CREATE TABLE Sample (Sample_id TEXT PRIMARY KEY, \
        Patient_id TEXT NOT NULL, Collection_date DATE NOT NULL, \
            Cancer_type TEXT NOT NULL, Mutation_count INTEGER, \
                Chemotherapy TEXT, Cytolytic_activity_score REAL, \
                    FOREIGN KEY (patient_id) \
                        REFERENCES Patient(patient_id)) """
)
conn.commit()

p1 = Patient(conn, "ABC")
p2 = Patient(conn, "DEF")
s1 = Sample(conn, "e2f8ybfg")
s2 = Sample(conn, "we8r32")
s3 = Sample(conn, "38fryv")


def test_add_patient():
    """Test if patient's record is added."""
    p1.add_patient("John Doe", "Male", "1980-1-1", 1234567890, "john@doe.com")
    p2.add_patient("Mike Tang", "Male", "1998-1-1", 234623820, "mike@ta.com")
    # Test p1
    c.execute("SELECT * from Patient where Patient_id = 'ABC'")
    result_1 = c.fetchall()
    assert result_1[0][0] == "ABC"
    assert result_1[0][1] == "John Doe"
    assert result_1[0][2] == "Male"
    assert result_1[0][3] == "1980-01-01 00:00:00"
    assert result_1[0][4] == 43
    assert result_1[0][5] == 1234567890
    assert result_1[0][6] == "john@doe.com"


def test_add_sample():
    """Test if sample's record is added."""
    s1.add_sample("ABC", "2019-3-3", "Breast Invasive Carcinoma", 9, "No", 1.5)
    s2.add_sample(
        "DEF", "2021-11-30", "Breast Invasive Ductal Carcinoma", 32, "No", 3.49
    )
    s3.add_sample("DEF", "2022-1-7", "Breast Invasive Carcinoma", 6, "No", 5.2)
    # Test s1
    c.execute("SELECT * from Sample where Sample_id = 'e2f8ybfg'")
    result = c.fetchall()
    assert result[0][0] == "e2f8ybfg"
    assert result[0][1] == "ABC"
    assert result[0][2] == "2019-03-03 00:00:00"
    assert result[0][3] == "Breast Invasive Carcinoma"
    assert result[0][4] == 9
    assert result[0][5] == "No"
    assert result[0][6] == 1.5


def test_update_patient():
    """Test if patient's record is updated."""
    p1.update_patient("Jack Wong", "Male", "1980-1-1", 12345678, "jack@w.com")
    c.execute("SELECT * FROM Patient WHERE Patient_id = 'ABC'")
    result = c.fetchall()
    assert result[0][0] == "ABC"
    assert result[0][1] == "Jack Wong"
    assert result[0][2] == "Male"
    assert result[0][3] == "1980-01-01 00:00:00"
    assert result[0][4] == 43
    assert result[0][5] == 12345678
    assert result[0][6] == "jack@w.com"


def test_update_sample():
    """Test if sample's record is updated."""
    s1.update_sample(
        "ABC", "2020-4-7", "Breast Invasive Lobular Carcinoma", 6, "No", 2.3
    )
    c.execute("SELECT * FROM Sample WHERE Sample_id = 'e2f8ybfg'")
    result = c.fetchall()
    assert result[0][0] == "e2f8ybfg"
    assert result[0][1] == "ABC"
    assert result[0][2] == "2020-04-07 00:00:00"
    assert result[0][3] == "Breast Invasive Lobular Carcinoma"
    assert result[0][4] == 6
    assert result[0][5] == "No"
    assert result[0][6] == 2.3


def test_delete_patient():
    """Test if patient's record is deleted."""
    # Check if p2 is deleted
    p2.delete_patient("DEF")
    c.execute("SELECT * FROM Patient WHERE Patient_id = 'DEF'")
    result = c.fetchone()
    assert result is None

    # Check if s2 and s3 are deleted
    c.execute("SELECT Sample_id FROM Sample WHERE Patient_id = 'DEF'")
    sample_ids = c.fetchall()
    assert len(sample_ids) == 0


def test_delete_sample():
    """Test if sample's record is deleted."""
    # Check if s1 is deleted
    s2.delete_sample("e2f8ybfg")
    c.execute("SELECT * FROM Sample WHERE Sample_id = 'e2f8ybfg'")
    result = c.fetchone()
    assert result is None

    # Check if table p1 still in patient
    c.execute(
        "SELECT Patient_id FROM Sample \
            WHERE Sample_id = 'e2f8ybfg'"
    )
    patient_ids = c.fetchall()
    assert len(patient_ids) == 0


def main() -> None:
    """Test."""
    test_add_patient()
    test_add_sample()
    test_update_patient()
    test_update_sample()
    test_delete_patient()
    test_delete_sample()


if __name__ == "__main__":
    main()
