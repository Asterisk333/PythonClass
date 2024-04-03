# Aufgabe3:
# Gegeben ist eine Liste von Dictionaries, wobei jedes Dictionary Informationen über Studenten enthält (
# name, matrikelnummer, und noten - eine Liste von Noten). Schreiben Sie ein Programm, das den Durchschnitt der Noten
# für jeden Studenten berechnet und diesen zusammen mit dem Namen in einem neuen Dictionary speichert. Sortieren Sie
# dieses Dictionary basierend auf den Durchschnittsnoten in absteigender Reihenfolge und geben Sie es aus

studenten = [
    {'name': 'Andrea', 'matrikelnummer': '123456', 'noten': [4.5, 6.0, 2.5]},
    {'name': 'Bernd', 'matrikelnummer': '234567', 'noten': [2.0, 5.3, 5.5]},
    {'name': 'Bernd der zweite', 'matrikelnummer': '345678', 'noten': [6.0, 6.0, 6.0]},
    {'name': 'Bernd der dritte', 'matrikelnummer': '456789', 'noten': [2.0, 1.0, 3.0]},
]

durchschnittsnoten = {}

for student in studenten:
    durchschnitt = sum(student['noten']) / len(student['noten'])
    durchschnittsnoten[student['name']] = durchschnitt

sorted_durchschnittsnoten = dict(sorted(durchschnittsnoten.items(), key=lambda item: item[1], reverse=True))

for name, durchschnitt in sorted_durchschnittsnoten.items():
    print(f"{name}: {durchschnitt}")
