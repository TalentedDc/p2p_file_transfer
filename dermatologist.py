from src.models.doctor import Doctor

class Dermatologist(Doctor):
    """Dermatologist extends Doctor with skin-care specific attributes and methods."""
    
    def __init__(self, person_id, name, age, gender, license_number, specialization,
                 skin_specialty, clinic_equipment):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.skin_specialty = skin_specialty  # e.g. "Cosmetic", "Medical", "Pediatric Dermatology"
        self.clinic_equipment = clinic_equipment if isinstance(clinic_equipment, list) else [clinic_equipment]
        # Authorship credit - put teammate's name here
        self.author = "Your Name"

    def diagnose_skin_condition(self, patient_name, symptoms):
        """Simulate dermatological diagnosis."""
        return f"Dr. {self.name} is diagnosing {patient_name} for {symptoms}. Specialty: {self.skin_specialty}"

    def recommend_treatment(self, condition):
        """Return basic treatment recommendation."""
        treatments = {
            "acne": "Topical retinoids + proper skincare routine",
            "eczema": "Moisturizers + topical corticosteroids", 
            "psoriasis": "Phototherapy + systemic medication"
        }
        return treatments.get(condition.lower(), "Refer for biopsy and further tests")

    def __str__(self):
        equipment = ", ".join(self.clinic_equipment)
        return (f"Dermatologist Dr. {self.name} - {self.skin_specialty} | "
                f"Equipment: {equipment} | Implemented by {self.author}")