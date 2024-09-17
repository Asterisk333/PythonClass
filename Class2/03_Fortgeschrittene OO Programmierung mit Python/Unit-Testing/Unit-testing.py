# Aufgabe 1: Schreibe Unittests für eine Funktion is_prime, die überprüft, ob eine gegebene Zahl n eine Primzahl ist.
# Schreibe Tests, um sicherzustellen, dass die Funktion für verschiedene Eingaben das erwartete Ergebnis liefert,
# sowohl für Primzahlen als auch für Nicht-Primzahlen.


import unittest


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


class TestIsPrime(unittest.TestCase):

    def test_less_than_2(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_prime_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))

    def test_non_prime_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(12))

    def test_large_prime_number(self):
        self.assertTrue(is_prime(7919))

    def test_large_non_prime_number(self):
        self.assertFalse(is_prime(7920))


# Aufgabe 2: Schreibe Unittests für eine Funktion calculate_average(numbers), die den Durchschnitt einer Liste von
# Zahlen berechnet. Überprüfe, ob die Funktion für verschiedene Eingaben den korrekten Durchschnitt zurückgibt,
# einschließlich leerer Listen und Listen mit negativen Zahlen.

def calculate_average(numbers):
    if not numbers:
        return False
    summe = 0
    laenge = 0
    for i in numbers:
        summe += i
        laenge += 1

    return summe / laenge


class TestCalculateAverage(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(calculate_average([]))

    def test_single_element_list(self):
        self.assertEqual(calculate_average([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3, -4, -5]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(calculate_average([-1, 0, 1]), 0)

    def test_large_numbers(self):
        self.assertEqual(calculate_average([1000000, 2000000, 3000000]), 2000000)

    def test_floats(self):
        self.assertAlmostEqual(calculate_average([1.5, 2.5, 3.5]), 2.5, )


# Aufgabe 3: Schreibe Unittests für eine Funktion reverse_string(s), die einen gegebenen String s umkehrt. Überprüfe,
# ob die Funktion für verschiedene Eingaben den erwarteten umgekehrten String zurückgibt, einschließlich leerer
# Strings und Strings mit Sonderzeichen.

def reverse_strings(s):
    if not s:
        return False
    return s[::-1]


class TestReverseStrings(unittest.TestCase):
    def test_empty_list(self):
        self.assertFalse(reverse_strings(""))
        self.assertFalse(reverse_strings(None))

    def test_single_element_list(self):
        self.assertEqual(reverse_strings("A"), "A")

    def test_strings(self):
        self.assertEqual(reverse_strings("Hello"), "olleH")

    def test_special_characters_mixed_case(self):
        self.assertEqual(reverse_strings("Hello!@#"), "#@!olleH")
