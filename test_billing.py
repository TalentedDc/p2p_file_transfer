"""
tests/test_billing.py

Tests for src/billing.py (Phase 8 - Billing System)

These use lightweight stand-in classes instead of importing the real
persons.py / services.py, so the tests don't break while those files are
still being built by teammates, and they double as a demonstration of
duck typing -- DuckService below is unrelated to any hospital service
class, yet billing_total() still works on it.

Once persons.py / services.py are finalised, swap the stand-ins below
for the real imports if you'd like these same assertions to run against
the actual classes too.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from billing import Bill, billing_total


# ---------- Stand-in classes (mimic persons.py / services.py) ----------

class DummyPatient:
    def __init__(self, has_nhis=False):
        self.has_nhis = has_nhis


class Consultation:
    def __init__(self, unit_cost_ngn):
        self.unit_cost_ngn = unit_cost_ngn


class DiagnosticTest:
    def __init__(self, unit_cost_ngn):
        self.unit_cost_ngn = unit_cost_ngn


class Procedure:
    def __init__(self, unit_cost_ngn):
        self.unit_cost_ngn = unit_cost_ngn


class DuckService:
    """Not related to any hospital service class at all -- just has the
    one attribute billing cares about. Proves duck typing works."""

    def __init__(self, unit_cost_ngn, name="Random Object"):
        self.unit_cost_ngn = unit_cost_ngn
        self.name = name


# ---------------------------- Tests ----------------------------

def test_duck_typing_billing_total():
    """billing_total() should work on ANY object with unit_cost_ngn,
    not just Consultation/DiagnosticTest/Procedure instances."""
    items = [Consultation(5000), DuckService(1200), Procedure(20000)]
    assert billing_total(items) == 5000 + 1200 + 20000


def test_duck_typing_missing_attribute_raises():
    class NotBillable:
        pass

    with pytest.raises(AttributeError):
        billing_total([NotBillable()])


def test_nhis_deduction_for_covered_services():
    patient = DummyPatient(has_nhis=True)
    bill = Bill(patient, [Consultation(10000), DiagnosticTest(8000)])
    expected_deduction = (10000 * 0.45) + (8000 * 0.45)
    assert bill.nhis_deductible_ngn == expected_deduction


def test_nhis_no_deduction_for_procedure():
    patient = DummyPatient(has_nhis=True)
    bill = Bill(patient, [Procedure(50000)])
    assert bill.nhis_deductible_ngn == 0.0


def test_no_nhis_means_no_deduction_at_all():
    patient = DummyPatient(has_nhis=False)
    bill = Bill(patient, [Consultation(10000), DiagnosticTest(8000)])
    assert bill.nhis_deductible_ngn == 0.0
    assert bill.net_payable_ngn == bill.gross_total_ngn


def test_net_payable_ngn():
    patient = DummyPatient(has_nhis=True)
    bill = Bill(patient, [Consultation(10000), Procedure(20000)])
    # Consultation gets 45% off, Procedure gets none
    expected_net = (10000 * 0.55) + 20000
    assert bill.net_payable_ngn == expected_net


def test_bill_addition():
    patient = DummyPatient(has_nhis=True)
    bill1 = Bill(patient, [Consultation(5000)])
    bill2 = Bill(patient, [Procedure(15000)])
    combined = bill1 + bill2
    assert len(combined.items) == 2
    assert combined.gross_total_ngn == 20000


def test_bill_addition_different_patients_raises():
    patient_a = DummyPatient(has_nhis=True)
    patient_b = DummyPatient(has_nhis=True)
    bill1 = Bill(patient_a, [Consultation(5000)])
    bill2 = Bill(patient_b, [Procedure(15000)])
    with pytest.raises(ValueError):
        bill1 + bill2


def test_itemized_bill_output():
    patient = DummyPatient(has_nhis=True)
    bill = Bill(patient, [Consultation(10000), Procedure(20000)])
    lines = bill.itemized_bill()

    assert len(lines) == 2
    assert lines[0]["item"] == "Consultation"
    assert lines[0]["unit_cost_ngn"] == 10000
    assert lines[0]["deduction_ngn"] == 4500
    assert lines[0]["payable_ngn"] == 5500

    assert lines[1]["item"] == "Procedure"
    assert lines[1]["deduction_ngn"] == 0
    assert lines[1]["payable_ngn"] == 20000
