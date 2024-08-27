# Aufgabe 1: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und eine neue
# Liste zurückgibt, in der jedes Wort großgeschrieben ist. Verwenden Sie dazu die map-Funktion und eine lambda-Funktion.
def capitalize_words(words):
    return list(map(lambda word: word.upper(), words))


# Beispiel
woerter = ["apfel", "banane", "kirsche"]
print(capitalize_words(woerter))  # Ausgabe: ['APFEL', 'BANANE', 'KIRSCHE']


# Aufgabe 2: Schreiben Sie eine Funktion in Python, die eine Liste von Zahlen als Parameter erhält und die Liste
# zurückgibt, sortiert nach der Anzahl der Ziffern in jeder Zahl. Verwenden Sie dazu die sorted-Funktion und eine
# lambda-Funktion.
def sort_by_digit_count(numbers):
    return sorted(numbers, key=lambda x: len(str(x)))


# Beispiel
zahlen = [123, 4, 56, 7890, 12]
print(sort_by_digit_count(zahlen))  # Ausgabe: [4, 12, 56, 123, 7890]


# Aufgabe 3: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und eine neue
# Liste zurückgibt, die nur die Wörter enthält, die ein Palindrom sind. Verwenden Sie dazu eine lambda-Funktion und
# die filter-Funktion.
def filter_palindromes(words):
    return list(filter(lambda word: word == word[::-1], words))


# Beispiel
woerter = ["anna", "banane", "otto", "kirsche"]
print(filter_palindromes(woerter))  # Ausgabe: ['anna', 'otto']


# Aufgabe 4: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und eine neue
# Liste zurückgibt, in der jedes Wort umgedreht ist. Verwenden Sie dazu die map-Funktion und eine lambda-Funktion.
def reverse_words(words):
    return list(map(lambda word: word[::-1], words))


# Beispiel
woerter = ["apfel", "banane", "kirsche"]
print(reverse_words(woerter))  # Ausgabe: ['lefpa', 'enananb', 'ehcsrik']
