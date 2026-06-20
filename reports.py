from datetime import date


def ward_report(ward):
    report = []

    report.append(
        f"WARD: {ward.ward_type}"
    )

    occupied = 0

    for bed in ward.beds:

        if bed.is_occupied:

            occupied += 1

            patient_name = (
                bed.patient.full_name
            )

            admission = (
                bed.admission_date.isoformat()
                if bed.admission_date
                else "N/A"
            )

            line = (
                f"Bed {bed.bed_number} | "
                f"Occupied | "
                f"{patient_name} | "
                f"{admission}"
            )

        else:

            line = (
                f"Bed {bed.bed_number} | "
                f"Empty"
            )

        report.append(line)

    occupancy = (
        occupied
        / ward.capacity
    ) * 100

    report.append("")
    report.append(
        f"Occupancy: "
        f"{occupancy:.0f}%"
    )

    return "\n".join(
        report
    )


def hospital_summary(hospital):
    """
    Generates summary of all wards.
    """

    lines = []

    lines.append(
        f"HOSPITAL: "
        f"{hospital.name}"
    )

    lines.append(
        f"Total Wards: "
        f"{len(hospital.wards)}"
    )

    total_beds = 0
    occupied = 0

    for ward in hospital.wards:

        total_beds += ward.capacity

        occupied += sum(
            1
            for bed in ward.beds
            if bed.is_occupied
        )

    available = (
        total_beds
        - occupied
    )

    occupancy = (
        occupied
        /
        total_beds
        * 100
        if total_beds
        else 0
    )

    lines.extend([
        f"Total Beds: {total_beds}",
        f"Occupied Beds: {occupied}",
        f"Available Beds: {available}",
        f"Occupancy: {occupancy:.0f}%"
    ])

    return "\n".join(
        lines
          )
