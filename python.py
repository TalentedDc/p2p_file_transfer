# src/persons.py

from abc import ABC, abstractmethod
from enum import Enum
from datetime import date

from validators import (
    validate_hospital_number,
    validate_staff_id,
)
from exceptions import ValidationError


class Person(ABC):
    """
    Abstract base class for all persons in the hospital system.
    """

    def __init__(self, full_name: str, person_id: str, birth_year: int):
        self.full_name = full_name
        self.person_id = person_id
        self._birth_year = birth_year

    @property
    def age(self) -> int:
        """Calculate age from birth year."""
        current_year = date.today().year
        return current_year - self._birth_year

    @abstractmethod
    def get_role(self):
        """Implemented by subclasses."""
        pass

    def __str__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.full_name}, id={self.person_id})"
        )

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"full_name='{self.full_name}', "
            f"person_id='{self.person_id}', "
            f"age={self.age})"
        )


class Patient(Person):
    """
    Hospital patient.
    """

    def __init__(
        self,
        full_name: str,
        person_id: str,
        birth_year: int,
        hospital_number: str,
        blood_group: str,
        genotype: str,
        nhis_number: str | None = None,
    ):
        super().__init__(full_name, person_id, birth_year)

        if not validate_hospital_number(hospital_number):
            raise ValidationError("Invalid hospital number.")

        self.hospital_number = hospital_number
        self.nhis_number = nhis_number
        self.blood_group = blood_group
        self.genotype = genotype
        self.appointments = []

    def get_role(self):
        return "Patient"


class Doctor(Person):
    """
    Medical doctor.
    """

    def __init__(
        self,
        full_name: str,
        person_id: str,
        birth_year: int,
        staff_id: str,
        specialisation: str,
        department: str,
    ):
        super().__init__(full_name, person_id, birth_year)

        if not validate_staff_id(staff_id):
            raise ValidationError("Invalid staff ID.")

        self.staff_id = staff_id
        self.specialisation = specialisation
        self.department = department

    def schedule_check(self):
        """
        Placeholder for doctor schedule validation/checking.
        """
        return True

    def get_role(self):
        return "Doctor"


class Shift(Enum):
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    NIGHT = "Night"


class Nurse(Person):
    """
    Hospital nurse.
    """

    def __init__(
        self,
        full_name: str,
        person_id: str,
        birth_year: int,
        ward_assignment: str,
        shift: Shift,
    ):
        super().__init__(full_name, person_id, birth_year)

        self.ward_assignment = ward_assignment
        self.shift = shift

    def get_role(self):
        return "Nurse"
