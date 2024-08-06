# Aufgabe 3 [10 Punkte]:
# Implementieren Sie ein Python-Programm, das die Häufigkeit des am wenigsten vorkommenden Zeichens in einem
# Python-String findet.

# Hinweis: Nutzen Sie ein Dictionary, pro Zeichen gibt es einen Eintrag. Der Wert des Eintrages entspricht
# der Häufigkeit.

satz = "Nutzen Sie ein Dictionary, pro Zeichen gibt es einen Eintrag. Der Wert des Eintrages entspricht der Häufigkeit."
buchstabenliste = {}

for buchstabe in satz.lower():
    if buchstabe in buchstabenliste:
        buchstabenliste[buchstabe] += 1
    else:
        buchstabenliste[buchstabe] = 1

min_buchstabe = None
min_menge = None

for buchstabe, menge in buchstabenliste.items():
    if min_buchstabe is None or menge < min_menge:
        min_buchstabe = buchstabe
        min_menge = menge

print(f"Der Buchstabe {min_buchstabe} kommt mit {min_menge} mal am wenigsten im Satz: {satz} vor")
