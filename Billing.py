"""
src/billing.py

Phase 8 - Billing System
Smart Hospital Appointment and Ward Management System

ASSUMPTIONS (since persons.py / services.py weren't available when this
was written -- adjust the helpers below once you see the real files):

  * A Patient-like object exposes NHIS status one of these ways, checked
    in order: a `has_valid_nhis()` method, a `has_nhis` attribute, a
    `nhis_valid` attribute, or an `nhis_status` string ("valid"/"active").
    See `_patient_has_nhis()`.

  * Any service item (Consultation, DiagnosticTest, Procedure, or
    anything else) only needs a numeric `unit_cost_ngn` attribute to be
    billable -- this is the duck typing requirement. To decide the NHIS
    deduction rate, we look at the item's class name. If services.py
    names its classes differently, update NHIS_DEDUCTION_RATES below.

  * Each item may optionally expose a `name` attribute for nicer
    itemized-bill labels; otherwise the class name is used.
"""

from typing import Iterable, List, Optional


# Deduction rate (as a fraction of unit_cost_ngn) applied per service type
# when the patient has valid NHIS cover.
NHIS_DEDUCTION_RATES = {
    "Consultation": 0.45,
    "DiagnosticTest": 0.45,
    "Procedure": 0.0,
}

# Any service class not listed above gets this default rate.
DEFAULT_DEDUCTION_RATE = 0.0


def billing_total(items: Iterable[object]) -> float:
    """
    Sum the unit_cost_ngn of any iterable of duck-typed items.

    Works with ANY object that has a `unit_cost_ngn` attribute -- it does
    NOT need to be a Consultation, DiagnosticTest, or Procedure instance.
    This is the duck-typing entry point required by the spec.
    """
    total = 0.0
    for item in items:
        cost = getattr(item, "unit_cost_ngn", None)
        if cost is None:
            raise AttributeError(
                f"{item!r} has no 'unit_cost_ngn' attribute; "
                "billing_total() requires duck-typed cost objects."
            )
        total += cost
    return total


def _patient_has_nhis(patient) -> bool:
    """Determine whether a patient has valid NHIS cover."""
    if hasattr(patient, "has_valid_nhis") and callable(patient.has_valid_nhis):
        return bool(patient.has_valid_nhis())
    if hasattr(patient, "has_nhis"):
        return bool(patient.has_nhis)
    if hasattr(patient, "nhis_valid"):
        return bool(patient.nhis_valid)
    if hasattr(patient, "nhis_status"):
        return str(patient.nhis_status).lower() in ("valid", "active", "true")
    return False


def _item_label(item) -> str:
    return getattr(item, "name", None) or getattr(item, "description", None) or type(item).__name__


def _deduction_rate_for(item) -> float:
    return NHIS_DEDUCTION_RATES.get(type(item).__name__, DEFAULT_DEDUCTION_RATE)


class Bill:
    """
    Represents a hospital bill made up of any number of duck-typed
    service items (each only needs a `unit_cost_ngn` attribute).
    """

    def __init__(self, patient, items: Optional[List[object]] = None):
        self.patient = patient
        self.items: List[object] = list(items) if items else []

    def add_item(self, item) -> None:
        """Add a single duck-typed service item to the bill."""
        if not hasattr(item, "unit_cost_ngn"):
            raise AttributeError(f"{item!r} cannot be billed: missing 'unit_cost_ngn'.")
        self.items.append(item)

    @property
    def gross_total_ngn(self) -> float:
        """Total cost before any NHIS deduction."""
        return billing_total(self.items)

    @property
    def nhis_deductible_ngn(self) -> float:
        """
        Total amount deducted because of NHIS cover.
        Returns 0 if the patient has no valid NHIS.
        """
        if not _patient_has_nhis(self.patient):
            return 0.0
        return sum(
            getattr(item, "unit_cost_ngn", 0) * _deduction_rate_for(item)
            for item in self.items
        )

    @property
    def net_payable_ngn(self) -> float:
        """What the patient actually has to pay after NHIS deduction."""
        return self.gross_total_ngn - self.nhis_deductible_ngn

    def itemized_bill(self) -> List[dict]:
        """
        Return a line-by-line breakdown of the bill:
        [{"item": ..., "unit_cost_ngn": ..., "deduction_ngn": ..., "payable_ngn": ...}, ...]
        """
        has_nhis = _patient_has_nhis(self.patient)
        lines = []
        for item in self.items:
            cost = getattr(item, "unit_cost_ngn", 0)
            rate = _deduction_rate_for(item) if has_nhis else 0.0
            deduction = cost * rate
            lines.append({
                "item": _item_label(item),
                "unit_cost_ngn": cost,
                "deduction_ngn": deduction,
                "payable_ngn": cost - deduction,
            })
        return lines

    def __add__(self, other: "Bill") -> "Bill":
        """Combine two bills for the SAME patient into one new Bill."""
        if not isinstance(other, Bill):
            return NotImplemented
        if self.patient is not other.patient:
            raise ValueError("Cannot add bills belonging to different patients.")
        return Bill(self.patient, self.items + other.items)

    def __repr__(self) -> str:
        return (
            f"Bill(patient={self.patient!r}, items={len(self.items)}, "
            f"gross={self.gross_total_ngn}, net={self.net_payable_ngn})"
        )
