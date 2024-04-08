import pytest
from app import bmi_calc

def test_bmi_calc():
    # Underweight tests
    assert bmi_calc(5, 10, 130)[1] == "Underweight"
    assert bmi_calc(5, 3, 100)[1] == "Underweight"

    # Normal weight tests
    assert bmi_calc(5, 9, 150)[1] == "Normal"
    assert bmi_calc(5, 11, 170)[1] == "Normal"

    # Overweight tests
    assert bmi_calc(5, 6, 190)[1] == "Overweight"
    assert bmi_calc(5, 4, 175)[1] == "Overweight"

    # Obese tests
    assert bmi_calc(6, 0, 250)[1] == "Obese"
    assert bmi_calc(5, 5, 220)[1] == "Obese"

