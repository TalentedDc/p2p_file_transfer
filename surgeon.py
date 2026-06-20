Prescription Management

from src.models.doctor import Doctor

class Surgeon(Doctor):
    """Surgeon extends Doctor with surgery-specific attributes and methods."""
    
    def __init__(self, person_id, name, age, gender, license_number, specialization, 
                 surgery_specialty, years_of_experience):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.surgery_specialty = surgery_specialty  # e.g. "Cardiothoracic", "Neurosurgery"
        self.years_of_experience = years_of_experience
        # Authorship credit for assessment
        self.author = "Emmanuel"

    def perform_surgery(self, patient_name, procedure):
        """Simulate
