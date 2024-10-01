import unittest
import math
from src.calculator import Calculator


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calculadora = Calculator()

    def test_suma(self):
        self.assertEqual(self.calculadora.suma(1, 2), 3)
        self.assertEqual(self.calculadora.suma(-1, -2), -3)
        self.assertEqual(self.calculadora.suma(1, -2), -1)
        self.assertEqual(self.calculadora.suma(0, 5), 5)

    def test_resta(self):
        self.assertEqual(self.calculadora.resta(5, 2), 3)
        self.assertEqual(self.calculadora.resta(-5, -2), -3)
        self.assertEqual(self.calculadora.resta(5, -2), 7)
        self.assertEqual(self.calculadora.resta(0, 5), -5)

    def test_multiplicacion(self):
        self.assertEqual(self.calculadora.multiplicacion(2, 3), 6)
        self.assertEqual(self.calculadora.multiplicacion(-2, -3), 6)
        self.assertEqual(self.calculadora.multiplicacion(2, -3), -6)
        self.assertEqual(self.calculadora.multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calculadora.division(6, 3), 2)
        self.assertEqual(self.calculadora.division(-6, -3), 2)
        self.assertEqual(self.calculadora.division(6, -3), -2)
        with self.assertRaises(ZeroDivisionError):
            self.calculadora.division(5, 0)
        self.assertEqual(self.calculadora.division(0, 5), 0)

    def test_raiz(self):
        self.assertEqual(self.calculadora.raiz(9), 3)
        self.assertEqual(self.calculadora.raiz(0), 0)
        with self.assertRaises(ValueError):
            self.calculadora.raiz(-1)

    def test_potencia(self):
        self.assertEqual(self.calculadora.potencia(2, 3), 8)
        self.assertEqual(self.calculadora.potencia(5, 0), 1)
        self.assertEqual(self.calculadora.potencia(-2, 3), -8)

    def test_seno(self):
        self.assertAlmostEqual(self.calculadora.seno(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(self.calculadora.seno(0), 0, places=5)

    def test_coseno(self):
        self.assertAlmostEqual(self.calculadora.coseno(0), 1, places=5)
        self.assertAlmostEqual(self.calculadora.coseno(math.pi), -1, places=5)

    def test_tangente(self):
        self.assertAlmostEqual(self.calculadora.tangente(0), 0, places=5)
        self.assertAlmostEqual(self.calculadora.tangente(math.pi / 4), 1, places=5)

    def test_factorial(self):
        self.assertEqual(self.calculadora.factorial(5), 120)
        self.assertEqual(self.calculadora.factorial(0), 1)
        self.assertEqual(self.calculadora.factorial(1), 1)
        self.assertEqual(self.calculadora.factorial(3), 6)
        self.assertEqual(self.calculadora.factorial(7), 5040)
        self.assertEqual(self.calculadora.factorial(10), 3628800)
        self.assertEqual(self.calculadora.factorial(-1), "Error: El factorial solo está definido para enteros no negativos.")
        self.assertEqual(self.calculadora.factorial(2.5), "Error: El factorial solo está definido para enteros no negativos.")
