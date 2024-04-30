# Entwickeln Sie eine Funktion in Python, die eine Liste von Listen akzeptiert, wobei jede innere Liste eine Reihe
# von ganzen Zahlen darstellt. Die Funktion soll ein neues Dictionary zurückgeben, in dem jeder Schlüssel die Summe
# der Zahlen in seiner entsprechenden Liste repräsentiert. Demonstrieren Sie die Funktionalität Ihrer Funktion mit
# einem Beispiel.

liste1 = [1, 2, 3, 4, 5, 6, 7, 8]
liste2 = [1, 2, 3, 4, 5, 6, 7]
liste3 = [1, 2, 3, 4, 5, 6]

listoflists = [liste1, liste2, liste3]

ergebnis = {}

for currentList in listoflists:
    sumlist = 0
    for number in currentList:
        sumlist += number
    ergebnis[sumlist] = currentList

print(ergebnis)
