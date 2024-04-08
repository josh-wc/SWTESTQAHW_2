import unittest
from app import bmi_calc

class TestBMICalculator(unittest.TestCase):

    def test_bmi_calc(self):
        # Underweight tests
        self.assertEqual(bmi_calc(5, 10, 130), ("Underweight", 18.5))
        self.assertEqual(bmi_calc(5, 10, 150), ("Underweight", 18.5))
        # Normal tests
        self.assertEqual(bmi_calc(5, 10, 151), ("Normal", 21.6))
        self.assertEqual(bmi_calc(5, 10, 160), ("Normal", 23.0))
        self.assertEqual(bmi_calc(5, 10, 190), ("Normal", 27.3))
        # Overweight tests
        self.assertEqual(bmi_calc(5, 10, 191), ("Overweight", 27.4))
        self.assertEqual(bmi_calc(5, 10, 200), ("Overweight", 28.7))
        self.assertEqual(bmi_calc(5, 10, 227.5), ("Overweight", 32.6))
        # Obese tests
        self.assertEqual(bmi_calc(5, 10, 228), ("Obese", 32.7))
        self.assertEqual(bmi_calc(5, 10, 240), ("Obese", 34.5))

if __name__ == '__main__':
    unittest.main()

