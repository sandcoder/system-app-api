from django.test import SimpleTestCase
from app import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Tests adding numbers together."""
        res = calc.add(10, 20)
        self.assertEqual(res, 30)

    def test_substract_numbers(self):
        """Test Substract numbers"""
        res = calc.substract(30, 10)
        self.assertEqual(res, 20)
