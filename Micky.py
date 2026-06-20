from datetime import datetime
import pytest

from appointments import Appointment
from exceptions import AppointmentConflictError


class DummyPerson:
    pass


class Consultation:
    pass


class DiagnosticTest:
    pass


class Procedure:
    pass


def make_appt(appt_id, start_time, service, duration=None):
    return Appointment(
        appt_id=appt_id,
        patient=DummyPerson(),
        doctor=DummyPerson(),
        scheduled_datetime=start_time,
        service_type=service,
        duration_min=duration,
    )


def test_equality():
    dt = datetime(2025, 1, 1, 9, 0)

    a1 = make_appt(1, dt, Consultation())
    a2 = make_appt(1, dt, Consultation())

    assert a1 == a2


def test_ordering():
    a1 = make_appt(
        1,
        datetime(2025, 1, 1, 9, 0),
        Consultation(),
    )

    a2 = make_appt(
        2,
        datetime(2025, 1, 1, 10, 0),
        Consultation(),
    )

    assert a1 < a2


def test_sorting():
    late = make_appt(
        2,
        datetime(2025, 1, 1, 11, 0),
        Consultation(),
    )

    early = make_appt(
        1,
        datetime(2025, 1, 1, 9, 0),
        Consultation(),
    )

    appts = [late, early]
    appts.sort()

    assert appts == [early, late]


def test_conflict_detection():
    a1 = make_appt(
        1,
        datetime(2025, 1, 1, 9, 0),
        Consultation(),
    )

    a2 = make_appt(
        2,
        datetime(2025, 1, 1, 9, 15),
        Consultation(),
    )

    with pytest.raises(AppointmentConflictError):
        a1.check_conflict(a2)


def test_no_conflict_case():
    a1 = make_appt(
        1,
        datetime(2025, 1, 1, 9, 0),
        Consultation(),
    )

    a2 = make_appt(
        2,
        datetime(2025, 1, 1, 9, 30),
        Consultation(),
    )

    assert a1.conflicts_with(a2) is False


def test_duration_calculation():
    appt = make_appt(
        1,
        datetime(2025, 1, 1, 9, 0),
        DiagnosticTest(),
    )

    assert appt.duration_min == 60
