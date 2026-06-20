import pytest
from src.services import MedicalService, Consultation, DiagnosticTest, Procedure
from src.persons import Patient

@pytest.fixture
def patient():
    return Patient("Ahmed Musa", "P001", 30, hospital_number="HOSP12345", 
                   blood_group="O+", genotype="AA")

def test_abc_cannot_instantiate():
    with pytest.raises(TypeError):
        MedicalService("S001", "Test", 1000)

def test_consultation_perform(patient):
    c = Consultation("CONS001", "General checkup", 5000)
    result = c.perform(patient)
    assert "Consultation performed" in result
    assert patient.full_name in result
    assert c.nhis_covered is True

def test_diagnostic_test_perform(patient):
    d = DiagnosticTest("DIAG001", "Blood test", 8000)
    result = d.perform(patient)
    assert "Diagnostic test performed" in result
    assert d.nhis_covered is True

def test_procedure_perform(patient):
    p = Procedure("PROC001", "Minor surgery", 50000)
    result = p.perform(patient)
    assert "Procedure performed" in result
    assert p.nhis_covered is False

def test_nhis_coverage_flags():
    assert Consultation("C1", "Test", 1000).nhis_covered is True
    assert DiagnosticTest("D1", "Test", 1000).nhis_covered is True
    assert Procedure("P1", "Test", 1000).nhis_covered is False

def test_validation():
    with pytest.raises(ValueError):
        Consultation("", "Test", 1000)
    with pytest.raises(ValueError):
        Procedure("P1", "Test", -500)