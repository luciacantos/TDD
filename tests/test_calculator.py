import unittest

from src.calculator import (suma, resta, multiplicacion, division)

class TestCalculadora(unittest.TestCase):

        def test_suma(self):
            self.assertEqual(suma(1, 2), 3)
            self.assertEqual(suma(-1, -2), -3)
            self.assertEqual(suma(1, -2), -1)
            self.assertEqual(suma(0, 5), 5)

        def test_resta(self):
            self.assertEqual(resta(5, 2), 3)
            self.assertEqual(resta(-5, -2), -3)
            self.assertEqual(resta(5, -2), 7)
            self.assertEqual(resta(0, 5), -5)

        def test_multiplicacion(self):
            self.assertEqual(multiplicacion(2, 3), 6)
            self.assertEqual(multiplicacion(-2, -3), 6)
            self.assertEqual(multiplicacion(2, -3), -6)
            self.assertEqual(multiplicacion(0, 5), 0)

        def test_division(self):
            self.assertEqual(division(6, 3), 2)
            self.assertEqual(division(-6, -3), 2)
            self.assertEqual(division(6, -3), -2)
            with self.assertRaises(ZeroDivisionError):
                division(5, 0)
            self.assertEqual(division(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
