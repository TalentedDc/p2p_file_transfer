class DepartmentHeadMixin:
    def __init__(self, *args, department_name=None, dept_budget=0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.department_name = department_name
        self.dept_budget = dept_budget

    def approve_budget(self, amount):
        if amount <= self.dept_budget:
            self.dept_budget -= amount
            return f"₦{amount:,.2f} approved for {self.department_name}. Remaining: ₦{self.dept_budget:,.2f}"
        return f"Budget request denied. Only ₦{self.dept_budget:,.2f} left in {self.department_name}"

    def allocate_budget(self, amount):
        self.dept_budget += amount
        return f"₦{amount:,.2f} added to {self.department_name} budget. Total: ₦{self.dept_budget:,.2f}"
