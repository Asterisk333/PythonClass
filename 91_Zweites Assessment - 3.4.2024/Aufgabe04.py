# Aufgabe4:
# Schreiben Sie ein Python-Programm, das zwei Listen A und B von Zahlen nimmt. Ihr Programm soll eine neue
# Liste C erstellen, die die Elemente enthält, die in beiden Listen vorkommen, ohne Duplikate. Demonstrieren Sie Ihr
# Programm mit den Listen A = [1, 2, 2, 3, 4] und B = [2, 3, 5, 6].

list_a = [1, 2, 2, 3, 4]
list_b = [2, 3, 5, 6]

list_c = []

list_d = list_a + list_b

for zahl in list_d:
    if zahl not in list_c:
        list_c.append(zahl)

print(list_c)
