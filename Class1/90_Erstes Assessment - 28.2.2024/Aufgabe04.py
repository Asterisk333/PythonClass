# Aufgabe 4 [10 Punkte]:
# Gegeben ist eine Liste von Elementen. Führen Sie eine Gruppierung ähnlicher Elemente durch, indem Sie verschiedene
# Schlüssel-Wert-Listen in einem Wörterbuch erstellen.

# Beispiele:
# Eingabe: test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
# Ausgabe : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}

test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
new_list = {}

for nummer in test_list:
    if nummer in new_list:
        new_list[nummer].append(nummer)
    else:
        new_list[nummer] = [nummer]

print(new_list)
