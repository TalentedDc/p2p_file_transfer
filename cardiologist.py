from src.models.doctor import Doctor

class Cardiologist(Doctor):
    """Cardiologist extends Doctor with heart-care specific attributes and methods."""

    def __init__(self, person_id, name, age, gender, license_number, specialization,
                 cardiac_specialty, equipment_available):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.cardiac_specialty = cardiac_specialty # e.g. "Interventional", "Electrophysiology", "Preventive"
        self.equipment_available = equipment_available if isinstance(equipment_available, list) else [equipment_available]
        # Authorship credit - put teammate's name here
        self.author = "Your Name"

    def perform_ecg(self, patient_name):
        """Simulate ECG test."""
        return f"Dr. {self.name} is performing ECG on {patient_name}. Equipment: {self.equipment_available[0]}"