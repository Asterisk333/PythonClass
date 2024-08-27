# Aufgabe 1: Schreibe eine Funktion, die eine Liste von Zahlen als Eingabe erhält und die Summe der Quadrate der
# geraden Zahlen zurückgibt.


def sum_of_even_squares(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squared_numbers = map(lambda x: x ** 2, even_numbers)
    return sum(squared_numbers)


# Beispielaufruf:
numbers_list = [1, 2, 3, 4, 5, 6]
result = sum_of_even_squares(numbers_list)
print("Summe der Quadrate der geraden Zahlen:", result)


# Aufgabe 2: Schreibe eine Funktion, die eine Liste von Strings als Eingabe erhält und eine Liste von Strings
# zurückgibt, die nur aus Großbuchstaben bestehen.


def filter_uppercase_strings(strings):
    return [s for s in strings if s.isupper()]


# Beispielaufruf:
string_list = ["Hello", "WORLD", "Python"]
uppercase_strings = filter_uppercase_strings(string_list)
print("Strings aus Großbuchstaben:", uppercase_strings)


# Aufgabe 3: Schreibe eine Funktion, die eine Liste von Strings als Eingabe erhält und eine Liste von Strings
# zurückgibt, die nur aus Zeichen bestehen, die in einem gegebenen Alphabet enthalten sind.


def filter_alphabet_strings(strings, alphabet):
    return [s for s in strings if all(c.lower() in alphabet.lower() for c in s)]


# Beispielaufruf:
string_list = ["Apple", "Banana", "Cherry", "123", "Dog", "abcde"]
given_alphabet = "abcde"
filtered_strings = filter_alphabet_strings(string_list, given_alphabet)
print("Strings im gegebenen Alphabet:", filtered_strings)
