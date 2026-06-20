import pytest
from src.persons import Doctor
from src.staff_roles import DepartmentHeadMixin, Consultant

def test_budget_addition():
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    c.add_budget(200000)
    assert c.dept_budget_ngn == 700000

def test_multiple_inheritance():
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    assert isinstance(c, Doctor)
    assert isinstance(c, DepartmentHeadMixin)
    assert isinstance(c, Consultant)

def test_mro_works():
    mro_names = [cls.__name__ for cls in Consultant.__mro__]
    assert mro_names[:4] == ["Consultant", "Doctor", "DepartmentHeadMixin", "Person"]

def test_consultant_has_doctor_features():
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    assert hasattr(c, "staff_id")
    assert hasattr(c, "specialisation")
    assert hasattr(c, "schedule_check")
    assert c.age == 45

def test_consultant_has_head_features():
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    assert hasattr(c, "dept_name")
    assert hasattr(c, "dept_budget_ngn")
    assert hasattr(c, "add_budget")
    c.add_budget(1000)
    assert c.dept_budget_ngn == 501000
