from src.models.doctor import Doctor
from src.models.department_head_mixin import DepartmentHeadMixin

class Consultant(DepartmentHeadMixin, Doctor):
    def __init__(self, person_id, name, age, gender, license_number, specialization, department_name, dept_budget):
        # MRO ensures both parent __init__ methods run
        super().__init__(
            person_id=person_id, name=name, age=age, gender=gender,
            license_number=license_number, specialization=specialization,
            department_name=department_name, dept_budget=dept_budget
        )
        # Authorship credit for assessment
        self.author = "Salawu Pelumi Dayo"

    def __str__(self):
        return f"Consultant Dr. {self.name} - Head of {self.department_name} | Implemented by {self.author}"
