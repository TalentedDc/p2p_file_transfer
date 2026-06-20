from exceptions import WardFullException, PatientNotFoundException
# If you need to type-hint the Patient object, you can import it here:
# from persons import Patient

class Bed:
    def __init__(self, bed_number: int, ward: 'Ward'):
        """
        Initializes a Bed instance.
        
        :param bed_number: Unique identifier for the bed within the ward.
        :param ward: Reference back to the parent Ward instance.
        """
        self.bed_number = bed_number
        self.ward = ward
        self.patient = None  # Holds a Patient object when occupied, None otherwise

    @property
    def is_occupied(self) -> bool:
        """Returns True if a patient is currently assigned to this bed."""
        return self.patient is not None

    def admit(self, patient) -> None:
        """Assigns a patient to this specific bed."""
        self.patient = patient

    def discharge(self) -> None:
        """Removes the patient from this bed, freeing it up."""
        self.patient = None


class Ward:
    def __init__(self, ward_id: str, ward_type: str, capacity: int):
        """
        Initializes a Ward instance and automatically creates its beds 
        based on the given capacity (Composition).
        """
        self.ward_id = ward_id
        self.ward_type = ward_type
        self.capacity = capacity
        
        # Composition: The Ward creates and manages its own collection of Beds
        self.beds = [Bed(bed_num, self) for bed_num in range(1, capacity + 1)]

    def admit(self, patient) -> Bed:
        """
        Finds the first available bed in the ward and admits the patient.
        Raises WardFullException if all beds are occupied.
        """
        for bed in self.beds:
            if not bed.is_occupied:
                bed.admit(patient)
                return bed
        
        # If loop finishes without returning, the ward is full
        raise WardFullException(f"Ward '{self.ward_id}' has reached its maximum capacity of {self.capacity}.")

    def discharge(self, patient) -> Bed:
        """
        Finds the bed holding the specified patient and vacates it.
        Raises PatientNotFoundException if the patient isn't in this ward.
        """
        for bed in self.beds:
            if bed.patient == patient:
                bed.discharge()
                return bed
                
        raise PatientNotFoundException(f"Patient not found in Ward '{self.ward_id}'.")
