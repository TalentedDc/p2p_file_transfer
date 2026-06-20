from datetime import date
from prescription import Prescription

# Assuming patient and doctor objects exist in your database
ampicillin_rx = Prescription(
    prescription_id="RX-2026-0942",
    patient=current_patient,         # Swapped with your actual Patient object
    doctor=doctor_sylvester,         # Swapped with your Doctor object (Dr. Sylvester)
    drug_name="Ampicillin",
    dosage="500mg",
    frequency="Every 6 hours (on an empty stomach)",
    duration_days=7,
    start_date=date.today()          # Sets to current date: June 20, 2026
)
