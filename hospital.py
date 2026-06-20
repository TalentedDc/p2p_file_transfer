class Hospital:

    def __init__(
        self,
        name
    ):

        self.name = name

        self.wards = []

    def add_ward(
        self,
        ward
    ):

        self.wards.append(
            ward
        )
