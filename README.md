## Featured Project — Smart Hospital Appointment and Ward Management System
A Python OOP system modelling administrative and clinical operations for a medium-sized Nigerian tertiary hospital. The system addresses paper-based workflows that commonly cause appointment clashes, lost prescriptions, and billing disputes by automating patient intake, scheduling, ward allocation, prescriptions, diagnostics, and billing with NHIS support.

Why it matters
- Many Nigerian hospitals still rely on manual paperwork; this system reduces errors, speeds patient flow, and improves accountability.
- NHIS-aware billing ensures insured patients receive correct deductions and itemised billing for transparency.

Core features
- Patient registration with NHIS support (verification fields and NHIS-deduction logic)
- Doctor scheduling across departments with conflict detection and availability windows
- Ward bed allocation by ward type (General, ICU, Maternity, Paediatric) with occupancy tracking
- Prescription lifecycle: creation, dispensing, modification, and history/audit trail
- Diagnostic test requests workflow and result linking
- Itemised bill computation with automatic NHIS deduction where applicable
- Role-based actors: Admin, Reception, Doctor, Nurse, Pharmacist, Accountant


  ## Team Members

    - Oyebode Omobolaji — CPE/2023/1101 — @TalentedDc
    - Oyetayo Michael — CPE/2023/1102 — @michaeloyetayo6-bit
    - Salawu Pelumi Dayo — CPE/2023/1105 — @pelumidayo43-art
    - Temitope Ayomiposi Gideon — CPE/2023/1110 — @prinposh
    - Shabi James Temiloluwa - CPE/2023/1107 - @dmfkrr000-sys
    - Uwaifo Ohiremen Paul - CPE/2023/1111 - @paul-3-maker
    - Popoola Emmanuel - CPE/2023/1104 - @Emmnel09
    - Shittu Daniel Oluwaseyi - CPE/2023/1108 - @Chicago003-ctrl
    - Owolabi Charles Kayode - CPE/2023/1100 - @64ytr5r6v9-spec
    - Sofoluwe Oreoluwa Ebenezer - CPE/2023/1109 - @dev-ore911
    - Abioye Gideon - CPE/2023/1112 - @Gsp149
    
## OOP Concepts Demonstrated
A table with examples and where they appear in the code. (Ensure each Week 1–5 concept appears at least once.)

| OOP Concept | Location in Code (file / class / lines) | Week |
|-------------|------------------------------------------|------|
| Encapsulation (properties & validation) | src/models/patient.py : class Patient (@property validators for nhis_id, contact) | Week 1 |
| Inheritance (Staff hierarchy) | src/models/staff.py : class Staff -> class Doctor, Nurse, Admin | Week 2 |
| Polymorphism (Appointment handlers) | src/services/scheduling_service.py : AppointmentHandler subclasses for Walk-in vs Booked | Week 3 |
| Composition (Ward contains Beds) | src/models/ward.py : Ward has list[Bed] -> Bed objects created/managed by Ward | Week 3 |
| Aggregation (Patient ↔ Prescription history) | src/models/prescription.py : Prescription stored in Patient.prescriptions list | Week 4 |
| Association (Patient — NHISAccount) | src/models/nhis_account.py and src/models/patient.py | Week 2 |
| Abstraction (BaseService) | src/services/base_service.py : BaseService abstract class for common service methods | Week 1 |
| Cohesion & SRP (BillingService computes itemised bills only) | src/services/billing_service.py | Week 5 |

## System Architecture
- Embed UML class diagram image: ../uml/class_diagram.png (also include source at uml/class_diagram.puml).
- High-level description (5–7 sentences):
  - The system follows a layered architecture separating domain models (src/models), business services (src/services), persistence/repositories, scripts for seeding/demo, and tests. Domain objects (Patient, NHISAccount, Staff, Ward, Bed, Prescription, Bill) encapsulate data and related behaviors. Services implement workflows (scheduling, ward allocation, prescriptions, billing) and coordinate model interactions. Composition is used for Ward→Bed (Ward "owns" Bed objects). Aggregation is used where Patient references but does not own external resources (e.g., historical records stored externally). The persistence layer is abstracted so the project can use SQLite for demo and PostgreSQL for production. Design choices favor high cohesion and single responsibility per class.

# How to Run
Exact commands to clone the repo, create venv, install deps, seed demo, and run tests.
- Clone the repo:
  - git clone https://github.com/TalentedDc/Smart-Hospital-Appointment-and-Ward-Management-System
  - cd smart-hospital-management-system
- Create and activate virtual environment:
  - python3 -m venv venv
  - source venv/bin/activate   # Linux/macOS
  - venv\Scripts\activate      # Windows (PowerShell: .\venv\Scripts\Activate.ps1)
- Install dependencies:
  - pip install -r requirements.txt
- Seed demo data and run a CLI demo:
  - python scripts/seed_demo.py
  - python main.py --demo
- Run tests:
  - pytest -q
- Notes: If using a real DB, configure DATABASE_URL in .env and run migrations (example with Alembic).

## Sample Output
Paste at least 8 lines of real console output showing the system working (example demo run):

```
[INFO] 2026-06-19 10:00:00 - Creating demo NHIS account for patient NG-000123
[INFO] 2026-06-19 10:00:01 - Registered Patient: John Doe (NHIS: NG-000123) — PatientID: P0001
[INFO] 2026-06-19 10:00:02 - Appointment scheduled: Dr. A. Okeke | Dept: Pediatrics | 2026-07-05 09:00
[INFO] 2026-06-19 10:00:03 - Ward allocation: Paediatric Ward �� Bed B-12 assigned to PatientID P0001
[INFO] 2026-06-19 10:00:04 - Prescription created: Amoxicillin 250mg x 7 days | PrescID: RX0009
[INFO] 2026-06-19 10:00:05 - Diagnostic requested: Full Blood Count | TestID: T-1002
[INFO] 2026-06-19 10:00:06 - Bill computed: Total=₦18,500.00 NHIS-covered=₦12,950.00 PatientPay=₦5,550.00
[INFO] 2026-06-19 10:00:07 - Payment recorded: Patient P0001 paid ₦5,550.00 via POS
[INFO] 2026-06-19 10:00:08 - Medication dispensed: Pharmacy confirmed RX0009 — qty dispensed: 7
[INFO] 2026-06-19 10:00:10 - Discharge summary generated for Patient P0001 — Records archived
```

## Known Limitations
- NHIS integration is simulated for demo; production requires secure API integration and authentication with NHIS services.
- Concurrency: current in-memory demo persistence has race conditions; production must use transactional DB and locks.
- No front-end UI included (CLI/demo only). UI and authentication/authorization are out of scope for the prototype.
- Scalability: designed for medium-sized hospitals; high-load multi-tenant deployment needs further refactor.
- Security: demo does not encrypt sensitive data nor implement full audit logging — must add before production.

 ## References
- Python documentation — https://docs.python.org/3/
- pytest documentation — https://docs.pytest.org/
- PlantUML — https://plantuml.com/
- National Health Insurance Scheme (NHIS) — https://www.nhis.gov.ng/ (for NHIS policy and contact)
- General OOP & Design Patterns references used during design (Gang of Four, SOLID principles)



