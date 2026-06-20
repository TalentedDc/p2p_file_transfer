from datetime import datetime, date, time

class Appointment:
    def __init__(self, 
                 appointment_id: str, 
                 patient, 
                 doctor, 
                 appointment_date: date, 
                 appointment_time: time, 
                 reason: str = "General Follow-up"):
        """
        Initializes an Appointment instance.
        
        :param appointment_id: Unique identifier for the appointment booking.
        :param patient: Reference to the Patient object (e.g., Bose).
        :param doctor: Reference to the Doctor object (e.g., Dr. Sylvester).
        :param appointment_date: The calendar date of the appointment.
        :param appointment_time: The specific clock time for the appointment.
        :param reason: Clinical reason for the visit.
        """
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time
        self.reason = reason
        self.status = "Scheduled"  # Options: Scheduled, Completed, Cancelled, No-Show

    @property
    def is_past(self) -> bool:
        """Returns True if the scheduled slot has already passed."""
        appointment_datetime = datetime.combine(self.appointment_date, self.appointment_time)
        return datetime.now() > appointment_datetime

    def cancel(self) -> None:
        """Cancels the appointment entry."""
        self.status = "Cancelled"

    def complete(self) -> None:
        """Marks the appointment as successfully completed by the clinician."""
        self.status = "Completed"

    def get_summary(self) -> str:
        """Generates a scannable summary string for notifications or logs."""
        patient_name = getattr(self.patient, 'name', 'Unknown Patient')
        doctor_name = getattr(self.doctor, 'name', 'Unknown Doctor')
        formatted_date = self.appointment_date.strftime("%B %d, %Y")
        formatted_time = self.appointment_time.strftime("%I:%M %p")
        
        return (
            f"Appointment ID: {self.appointment_id} [{self.status}]\n"
            f"Patient: {patient_name}\n"
            f"Provider: Dr. {doctor_name}\n"
            f"Date/Time: {formatted_date} at {formatted_time}\n"
            f"Reason: {self.reason}"
        )
      from datetime import date, time
from appointment import Appointment

# Mock entity objects tracking back to your database or person modules
class Patient:
    def __init__(self, name: str):
        self.name = name

class Doctor:
    def __init__(self, name: str):
        self.name = name

# 1. Instantiate the target entities
patient_bose = Patient(name="Bose")
doctor_sylvester = Doctor(name="Sylvester")

# 2. Book the appointment 
sylvester_bose_appointment = Appointment(
    appointment_id="APT-2026-0045",
    patient=patient_bose,
    doctor=doctor_sylvester,
    appointment_date=date(2026, 6, 25),      # June 25, 2026
    appointment_time=time(10, 30),           # 10:30 AM
    reason="Post-op review for Ampicillin response"
)

# 3. Output the digital booking details
print(sylvester_bose_appointment.get_summary())
Appointment ID: APT-2026-0045 [Scheduled]
Patient: Bose
Provider: Dr. Sylvester
Date/Time: June 25, 2026 at 10:30 AM
Reason: Post-op review for Ampicillin response

