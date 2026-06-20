# tests/test_persons.py

import pytest

from src.persons import (
    Person,
    Patient,
    Doctor,
    Nurse,
    Shift,
)
from exceptions import ValidationError


def test_person_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Person("John Doe", "P001", 1990)


def test_age_calculation():
    patient = Patient(
        full_name="Jane Doe",
        person_id="P001",
        birth_year=2000,
        hospital_number="HN001",
        blood_group="O+",
        genotype="AA",
    )

    assert patient.age > 0


def test_patient_validation():
    with pytest.raises(ValidationError):
        Patient(
            full_name="Jane Doe",
            person_id="P001",
            birth_year=2000,
            hospital_number="INVALID",
            blood_group="O+",
            genotype="AA",
        )


def test_doctor_validation():
    with pytest.raises(ValidationError):
        Doctor(
            full_name="Dr Smith",
            person_id="D001",
            birth_year=1980,
            staff_id="INVALID",
            specialisation="Cardiology",
            department="Medicine",
        )


def test_nurse_creation():
    nurse = Nurse(
        full_name="Mary Johnson",
        person_id="N001",
        birth_year=1995,
        ward_assignment="Ward A",
        shift=Shift.NIGHT,
    )

    assert nurse.ward_assignment == "Ward A"
    assert nurse.shift == Shift.NIGHT


def test_str_method():
    patient = Patient(
        full_name="Jane Doe",
        person_id="P001",
        birth_year=2000,
        hospital_number="HN001",
        blood_group="O+",
        genotype="AA",
    )

    assert "Jane Doe" in str(patient)


def test_repr_method():
    patient = Patient(
        full_name="Jane Doe",
        person_id="P001",
        birth_year=2000,
        hospital_number="HN001",
        blood_group="O+",
        genotype="AA",
    )

    assert "Patient" in repr(patient)
