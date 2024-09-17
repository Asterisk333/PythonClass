# Aufgabe: Testen einer mathematischen Funktion
#  Sie einen Unittest, um die Funktion factorial zu testen, die die Fakultät einer gegebenen Zahl n berechnet.
import math
import unittest


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        return False
    else:
        return n * factorial(n - 1)


class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)


# Aufgabe: Testen einer Klasse
# Schreiben Sie einen Unittest, um die Klasse Kreis zu testen, die einen Kreis
# repräsentiert und Methoden zur Berechnung der Fläche bereitstellt.

class Kreis:
    def __init__(self, radius):
        self.radius = radius

    def berechne_flaeche(self):
        return math.pi * (self.radius ** 2)


class TestKreis(unittest.TestCase):
    def test_berechne_flaeche(self):
        kreis = Kreis(5)
        self.assertEqual(kreis.berechne_flaeche(), math.pi * (5 ** 2))

    def test_berechne_flaeche_mit_null_radius(self):
        kreis = Kreis(0)
        self.assertEqual(kreis.berechne_flaeche(), 0)

    def test_berechne_flaeche_mit_negativem_radius(self):
        kreis = Kreis(-5)
        self.assertEqual(kreis.berechne_flaeche(), math.pi * (5 ** 2))

