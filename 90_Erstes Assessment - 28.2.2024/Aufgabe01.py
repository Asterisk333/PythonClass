# Aufgabe 1 [10 Punkte]:
# Gegeben ist eine Liste von Zahlen. Die Aufgabe besteht darin, ein Python-Programm zu schreiben, das die zweitgrößte
# Zahl in der gegebenen Liste findet.
# Beispiel.
# Eingabe: list1 = [10, 20, 4]
# Ausgabe: 10
# Eingabe: list2 = [70, 11, 20, 4, 100]
# Ausgabe: 70

liste = [70, 11, 20, 4, 100]

groesste = None
zweitgroesste = None

for element in liste:
    if groesste is None or element > groesste:
        zweitgroesste = groesste
        groesste = element
    elif zweitgroesste is None or element > zweitgroesste:
        zweitgroesste = element

print(zweitgroesste)
