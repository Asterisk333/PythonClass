# Schreiben Sie ein Python-Programm zum Entfernen von Duplikaten aus einer Liste

liste = ["alpha", "beta", "gamma", "alpha"]
ergebnis = []

for element in liste:
    if element not in ergebnis:
        ergebnis.append(element)

# Die Ergebnisliste ausgeben
print(ergebnis)
