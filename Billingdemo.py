"""
examples/billing_demo.py

A runnable walkthrough of the billing system (Phase 8).

Run with:
    python examples/billing_demo.py

This uses lightweight stand-in Patient/Service classes (the same ones
used in tests/test_billing.py) since persons.py / services.py weren't
available yet. Swap them for the real imports once those files exist.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from billing import Bill, billing_total


# ---------- Stand-in classes (swap for real persons.py / services.py) ----------

class Patient:
    def __init__(self, name, has_nhis):
        self.name = name
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


def print_itemized(bill):
    print(f"\nItemized bill for {bill.patient.name}:")
    print(f"{'Item':<20}{'Cost (NGN)':>15}{'Deduction':>15}{'Payable':>15}")
    for line in bill.itemized_bill():
        print(
            f"{line['item']:<20}"
            f"{line['unit_cost_ngn']:>15,.2f}"
            f"{line['deduction_ngn']:>15,.2f}"
            f"{line['payable_ngn']:>15,.2f}"
        )
    print("-" * 65)
    print(f"{'Gross total':<35}{bill.gross_total_ngn:>15,.2f}")
    print(f"{'NHIS deductible':<35}{bill.nhis_deductible_ngn:>15,.2f}")
    print(f"{'Net payable':<35}{bill.net_payable_ngn:>15,.2f}")


def main():
    # --- Patient WITH valid NHIS ---
    chidi = Patient(name="Chidi Okafor", has_nhis=True)
    morning_bill = Bill(chidi, [
        Consultation(5000),
        DiagnosticTest(12000),
    ])
    afternoon_bill = Bill(chidi, [
        Procedure(35000),
    ])

    full_day_bill = morning_bill + afternoon_bill
    print_itemized(full_day_bill)

    # --- Patient WITHOUT NHIS ---
    amaka = Patient(name="Amaka Eze", has_nhis=False)
    amaka_bill = Bill(amaka, [
        Consultation(5000),
        Procedure(35000),
    ])
    print_itemized(amaka_bill)

    # --- Duck typing demo: a totally unrelated object still works ---
    class WalkInFee:
        def __init__(self, unit_cost_ngn):
            self.unit_cost_ngn = unit_cost_ngn
            self.name = "Walk-in Registration Fee"

    misc_total = billing_total([Consultation(5000), WalkInFee(500)])
    print(f"\nDuck typing demo -- billing_total() on mixed objects: "
          f"NGN {misc_total:,.2f}")


if __name__ == "__main__":
    main()
