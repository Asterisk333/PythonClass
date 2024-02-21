# Es seien zwei Listen gegeben. Schreiben Sie eine Python-Funktion, um sie so in ein Dictionary umzuwandeln, dass der Eintrag aus Liste1 der Schlüssel und der Eintrag aus Liste2 der Wert ist.
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Ergebnis:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


# Definiere die Listen
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Verwende die dict-Funktion, um das Dictionary zu erstellen
print(dict(zip(keys, values)))
