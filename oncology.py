from src.models.doctor import Doctor

class Oncologist(Doctor):
    """Oncologist extends Doctor with cancer-care specific attributes and methods."""

    def __init__(self, person_id, name, age, gender, license_number, specialization,
                 cancer_type, treatment_methods):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.cancer_type = cancer_type # e.g. "Breast", "Lung", "Blood/Lymphoma"
        self.treatment