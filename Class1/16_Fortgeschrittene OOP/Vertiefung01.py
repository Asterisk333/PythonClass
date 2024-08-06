# Einkaufsliste Programm Erstelle ein Python-Programm, das eine Einkaufsliste verwaltet. Die Einkaufsliste soll als
# Liste von Strings repräsentiert werden. Dein Programm soll Folgendes können:

# Hinzufügen eines neuen Artikels zur Liste.
# Entfernen eines Artikels aus der Liste.
# Anzeigen aller Artikel in der Liste in einer formatierten Ausgabe.
# Bonus: Verhindere das Hinzufügen von Duplikaten und implementiere eine Funktion,
# die überprüft, ob ein Artikel bereits in der Liste ist.

# Initialisiere eine leere Liste für die Einkaufsliste
einkaufsliste = []


# Funktion zum Hinzufügen eines Artikels zur Einkaufsliste
def artikel_hinzufuegen(artikel):
    # Überprüfe, ob der Artikel bereits in der Liste ist, um Duplikate zu vermeiden
    if artikel not in einkaufsliste:
        einkaufsliste.append(artikel)  # Füge den Artikel hinzu
        print(f"{artikel} wurde zur Liste hinzugefügt.")
    else:
        print(f"{artikel} ist bereits in der Liste.")


# Funktion zum Entfernen eines Artikels aus der Einkaufsliste
def artikel_entfernen(artikel):
    # Überprüfe, ob der Artikel in der Liste ist
    if artikel in einkaufsliste:
        einkaufsliste.remove(artikel)  # Entferne den Artikel
        print(f"{artikel} wurde aus der Liste entfernt.")
    else:
        print(f"{artikel} war nicht in der Liste.")


# Funktion zum Anzeigen aller Artikel in der Einkaufsliste
def liste_anzeigen():
    print("Einkaufsliste:")
    for artikel in einkaufsliste:
        print(f"- {artikel}")


# Beispielverwendung der Funktionen
artikel_hinzufuegen("Äpfel")
artikel_entfernen("Brot")
liste_anzeigen()
