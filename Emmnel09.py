import pytest
from src.staff_roles import Consultant, DepartmentHeadMixin
from src.persons import Doctor

def test_budget_addition():
    """Required Test: Budget addition"""
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    c.add_budget(200000)
    assert c.dept_budget_ngn == 700000
    assert c.add_budget(50000) == 750000

def test_multiple_inheritance():
    """Required Test: Multiple inheritance"""
    c = Consultant("Aisha Bello", "P001", 45, "STF1001", "Cardiology", "Medicine",
                   dept_name="Cardiology", dept_budget_ngn=500000)
    assert isinstance(c, Consultant)
    assert isinstance(c, Doctor)
    assert isinstance(c, DepartmentHeadMixin)

def test_mro_works():
    """Required Test: MRO works - Consultant -> Doctor -> DepartmentHeadMixin -> Person"""
    mro_names = [cls.__name__ for cls in Consultant.__mro__]
    assert mro_names[0] == "Consultant"
    assert mro_names[1] == "Doctor"
    assert mro_names[2] == "DepartmentHeadMixin"
    assert "Person" in mro_names

def test_consultant_has_doctor_features():
    """Required Test: Consultant has Doctor features"""
    c = Consultant("Aisha", "P001", 45, "STF1001", "Cardiology", "Medicine", "Cardiology", 500000)
    # From Doctor
    assert hasattr(c, "staff_id")
    assert hasattr(c, "specialisation")
    assert hasattr(c, "department")
    assert hasattr(c, "schedule_check")
    assert c.staff_id == "STF1001"
    assert c.specialisation == "Cardiology"
    # From Person
    assert c.age == 45
    assert c.full_name == "Aisha"

def test_consultant_has_head_features():
    """Required Test: Consultant has Head features"""
    c = Consultant("Aisha", "P001", 45, "STF1001", "Cardiology", "Medicine", "Cardiology", 500000)
    # From DepartmentHeadMixin
    assert hasattr(c, "dept_name")
    assert hasattr(c, "dept_budget_ngn")
    assert hasattr(c, "add_budget")
    assert c.dept_name == "Cardiology"
    assert c.dept_budget_ngn == 500000
    assert str(c).startswith("Consultant")
