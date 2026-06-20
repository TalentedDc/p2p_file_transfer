from datetime import date


class Bed:

    def __init__(
        self,
        bed_number
    ):
        self.bed_number = bed_number

        self.patient = None

        self.admission_date = None

    @property
    def is_occupied(self):

        return (
            self.patient
            is not None
        )

    def admit(
        self,
        patient
    ):

        self.patient = patient

        self.admission_date = (
            date.today()
        )

    def discharge(
        self
    ):

        self.patient = None

        self.admission_date = None


class Ward:

    def __init__(
        self,
        ward_id,
        ward_type,
        capacity
    ):

        self.ward_id = ward_id

        self.ward_type = ward_type

        self.capacity = capacity

        self.beds = [
            Bed(i + 1)
            for i in range(
                capacity
            )
      ]
