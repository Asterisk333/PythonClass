# Gegeben ist eine Liste von Dictionaries, wobei jedes Dictionary Informationen über Mitarbeiter enthält (Name,
# Abteilung und Gehalt). Schreiben Sie ein Programm, das den Durchschnitt des Gehalts für jeden Mitarbeiter berechnet
# und diesen zusammen mit dem Namen in einem neuen Dictionary speichert. Sortieren Sie dieses Dictionary basierend
# auf den Gehältern in absteigender Reihenfolge und geben Sie es aus.

mitarbeiter_liste = [
    {'Name': 'herbert olaf', 'Abteilung': 'IT', 'Gehalt': 70000},
    {'Name': 'karin keller', 'Abteilung': 'HR', 'Gehalt': 65000},
]

durchschnittsgehalt_dict = {mitarbeiter['Name']: mitarbeiter['Gehalt'] for mitarbeiter in mitarbeiter_liste}

print(durchschnittsgehalt_dict)
