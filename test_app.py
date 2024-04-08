import unittest
from app import bmi_calc, weight_input, height_feet_input, height_inches_input
from unittest import mock


def test_height_feet_input(mock_input):
    mock_input.extend(['1', '2', '6', '8', '10'])
    assert height_feet_input() > 0 and height_feet_input() <= 9

def test_height_inches_input(mock_input):
    mock_input.extend(['2', '3', '7', '11', '13'])
    assert height_inches_input() > 0 and height_inches_input() <= 12

def test_weight_input(mock_input):
    mock_input.extend(['50', '100', '250', '500', '550'])
    assert weight_input() > 0 and weight_input() <= 500

def test_bmi_calc():
    # Underweight tests
    assert bmi_calc(5, 10, 130) == "Underweight" and bmi_calc(5, 10, 150) == "Underweight"
    # Normal tests
    assert bmi_calc(5, 10, 151) == "Normal" and bmi_calc(5, 10, 160) == "Normal" and bmi_calc(5, 10, 190) == "Normal"
    # Overweight tests
    assert bmi_calc(5, 10, 191) == "Overweight" and bmi_calc(5, 10, 200) == "Overweight" and bmi_calc(5, 10, 227.5) == "Overweight"
    # Obese tests
    assert bmi_calc(5, 10, 228) == "Obese" and bmi_calc(5, 10, 240) == "Obese"
