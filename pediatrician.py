from src.models.doctor import Doctor

class Pediatrician(Doctor):
    """Pediatrician extends Doctor with child-care specific attributes and methods."""
    
    def __init__(self, person_id, name, age, gender, license_number, specialization,
                 age_group, vaccination_certified):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.age_group = age_group  # e.g. "Neonates", "Children 0-12", "Adolescents"
        self.vaccination_certified = vaccination_certified if isinstance(vaccination_certified, list) else [vaccination_certified]
        # Authorship credit - put teammate's name here
        self.author = "Your Name"

    def check_child_growth(self, child_name, height_cm, weight_kg):
        """Basic growth check simulation."""
        bmi = weight_kg / ((height_cm/100) ** 2)