# Aufgabe 5 [10 Punkte]:
# Gegeben ist eine Liste von Elementen. Die Aufgabe besteht darin, ein Python-Programm zu schreiben, um alle Indizes
# aller Elemente zu berechnen und in ein Dictionary zu speichern. Beispiel:

# Eingabe: test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
# Ausgabe: {8: [4, 8], 3: [2, 5], 6: [1, 6], 7: [0, 3, 7]}
# Erklärung: Die Zahl 8 tritt an der 4. und 8. Stelle auf, die Zahl 3 tritt an der 2. und 5. Stelle auf usw.

test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
laenge = len(test_list)
new_list = {}

for counter in range(laenge):
    nummer = test_list[counter]
    if nummer in new_list:
        new_list[nummer].append(counter)
    else:
        new_list[nummer] = [counter]

print(new_list)
