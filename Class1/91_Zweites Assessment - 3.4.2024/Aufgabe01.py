# Aufgabe1:
# Implementieren Sie eine Funktion in Python, die ein Dictionary akzeptiert, dessen Schlüssel Strings und
# deren Werte Listen von Zahlen sind. Die Funktion soll ein neues Dictionary zurückgeben, in dem jeder Schlüssel die
# Summe der Zahlen in seiner Liste repräsentiert. Demonstrieren Sie die Funktionalität Ihrer Funktion mit einem
# Beispiel-Dictionary.

def summen_der_listen(directory):
    summen_dict = {}
    for key, werte_liste in directory.items():
        summen_dict[key] = sum(werte_liste)
    return summen_dict


bsp_dict = {
    'a': [1, 2, 3],
    'b': [2, 3, 4]
}

summiert = summen_der_listen(bsp_dict)
print(summiert)
