from src.models.doctor import Doctor

class Radiographer(Doctor):
    """Radiographer extends Doctor with imaging/radiology-specific attributes."""
    
    def __init__(self, person_id, name, age, gender, license_number, specialization,
                 imaging_type, equipment_certified):
        # Call Doctor __init__ via super()
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization
        )
        self.imaging_type = imaging_type  # e.g. "X-Ray", "MRI", "CT-Scan", "Ultrasound"
        self.equipment_certified = equipment_certified  # list of machines they can operate
        # Authorship credit - put your name here
        self.author = "Your Name"

    def perform_scan(self, patient_name, scan_type):
        """Simulate performing a radiological scan."""
        if scan_type not in self.equipment_certified:
            return f"Dr. {self.name} is not certified for {scan_type} scans"
        return f"Dr. {self.name} is performing {scan_type} scan on {patient_name}. Equipment: {self.imaging_type}"

    def __str__(self):
        equipment = ", ".join(self.equipment_certified) if isinstance(self.equipment_certified, list) else self.equipment_certified
        return (f"Radiographer Dr. {self.name} - {self.imaging_type} | "
                f"Certified: {equipment} | Implemented by {self.author}")
