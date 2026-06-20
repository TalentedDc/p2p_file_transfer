from .persons import Doctor

class DepartmentHeadMixin:
    """
    Mixin to add department head responsibilities to a Doctor.
    Must be used with multiple inheritance alongside Doctor.
    """
    def __init__(self, *args, dept_name=None, dept_budget_ngn=0, **kwargs):
        # Let Doctor.__init__ run first via super()
        super().__init__(*args, **kwargs)
        self.dept_name = dept_name
        self.dept_budget_ngn = int(dept_budget_ngn)

    def add_budget(self, amount_ngn):
        """Add budget to department. amount must be non-negative."""
        if not isinstance(amount_ngn, (int, float)):
            raise TypeError("amount_ngn must be int or float")
        if amount_ngn < 0:
            raise ValueError("amount_ngn must be >= 0")
        self.dept_budget_ngn += int(amount_ngn)
        return self.dept_budget_ngn

    def __repr__(self):
        base = super().__repr__()
        return f"{base[:-1]}, dept_name='{self.dept_name}', dept_budget_ngn={self.dept_budget_ngn})"

class Consultant(Doctor, DepartmentHeadMixin):
    """
    Consultant = Doctor + Department Head.
    MRO: Consultant -> Doctor -> DepartmentHeadMixin -> Person -> ABC -> object
    super() ensures both Doctor.__init__ and DepartmentHeadMixin.__init__ run.
    """
    def __init__(self, full_name, person_id, age, staff_id, specialisation, department,
                 dept_name, dept_budget_ngn=0):
        super().__init__(
            full_name=full_name,
            person_id=person_id,
            age=age,
            staff_id=staff_id,
            specialisation=specialisation,
            department=department,
            dept_name=dept_name,
            dept_budget_ngn=dept_budget_ngn
        )

    def __str__(self):
        return f"Consultant {self.full_name} - {self.specialisation}, Head of {self.dept_name}"
