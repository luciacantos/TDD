import math

class Calculator():

    def __init__(self):
        self.value = 0

    def suma(self, a, b):
        self.value = a + b
        return self.value

    def resta(self, a, b):
        self.value = a - b
        return self.value

    def multiplicacion(self, a, b):
        self.value = a * b
        return self.value

    def division(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Error: No se puede dividir por cero.")
        self.value = a / b
        return self.value

    def raiz(self, a):
        if a < 0:
            return "Error: No se puede calcular la raíz de un número negativo."
        self.value = math.sqrt(a)
        return self.value

    def potencia(self, a, b):
        self.value = a ** b
        return self.value

    def seno(self, a):
        self.value = math.sin(a)
        return self.value

    def coseno(self, a):
        self.value = math.cos(a)
        return self.value

    def tangente(self, a):
        self.value = math.tan(a)
        return self.value

    def factorial(self, a):
        if not isinstance(a, int) or a < 0:
            return "Error: El factorial solo está definido para enteros no negativos."
        fact = 1
        for i in range(1, a + 1):
            fact *= i
        self.value = fact
        return self.value

    def __str__(self):
        return str(self.value)
