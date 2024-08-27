# Aufgabe 1: Schreiben Sie eine Funktion in Python, die eine Liste von Zahlen als Parameter erhält und die Summe
# aller geraden Zahlen in der Liste zurückgibt.
def sum_even_numbers(numbers):
    return sum(filter(lambda x: x % 2 == 0, numbers))


# Beispiel
zahlen = [1, 2, 3, 4, 5, 6]
print(sum_even_numbers(zahlen))  # Ausgabe: 12


# Aufgabe 2: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und eine Liste
# von Tupeln zurückgibt, die jedes Wort in der Liste zusammen mit seiner Länge enthält.
def words_with_lengths(words):
    return list(map(lambda word: (word, len(word)), words))


# Beispiel
woerter = ["Apfel", "Banane", "Kirsche"]
print(words_with_lengths(woerter))  # Ausgabe: [('Apfel', 5), ('Banane', 6), ('Kirsche', 7)]


# Aufgabe 3: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und die Liste der
# Wörter zurückgibt, die mit einem bestimmten Buchstaben beginnen. Verwenden Sie dabei eine lambda-Funktion.
def words_starting_with_letter(words, letter):
    return list(filter(lambda word: word.startswith(letter), words))


# Beispiel
woerter = ["Apfel", "Banane", "Avocado", "Kirsche"]
print(words_starting_with_letter(woerter, 'A'))  # Ausgabe: ['Apfel', 'Avocado']


# Aufgabe 4: Schreiben Sie eine Funktion in Python, die eine Liste von Wörtern als Parameter erhält und eine Liste
# von Wörtern zurückgibt, die mehr als 5 Buchstaben haben und mit einem Vokal enden. Verwenden Sie dabei die
# filter-Funktion und eine lambda-Funktion.
def words_with_specific_criteria(words):
    vowels = 'aeiou'
    return list(filter(lambda word: len(word) > 5 and word[-1].lower() in vowels, words))


# Beispiel
woerter = ["Apfel", "Banane", "Avocado", "Kirsche", "Erdbeere"]
print(words_with_specific_criteria(woerter))  # Ausgabe: ['Banane', 'Avocado', 'Erdbeere']
