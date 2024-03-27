# Adressbuch Programm Implementiere ein einfaches Adressbuch mit Python, das Dictionaries verwendet. Jeder Eintrag im
# Adressbuch soll den Namen einer Person (als Schlüssel) und weitere Informationen wie E-Mail und Telefonnummer (als
# Dictionary) enthalten. Das Programm soll folgende Funktionen haben:

# einer neuen Person zum Adressbuch.
# Löschen einer Person aus dem Adressbuch.
# Suchen der Kontaktdaten (E-Mail, Telefonnummer) einer Person.
# Bonus: Füge die Möglichkeit hinzu, die Informationen einer Person zu aktualisieren.

# Initialisiere ein leeres Dictionary für das Adressbuch
adressbuch = {}


# Funktion zum Hinzufügen einer neuen Person zum Adressbuch
def person_hinzufuegen(name, email, telefonnummer):
    # Überprüfe, ob der Name bereits ein Schlüssel im Adressbuch ist
    if name not in adressbuch:
        # Erstelle einen neuen Eintrag mit Email und Telefonnummer
        adressbuch[name] = {"Email": email, "Telefonnummer": telefonnummer}
        print(f"{name} wurde zum Adressbuch hinzugefügt.")
    else:
        print(f"{name} ist bereits im Adressbuch.")


# Funktion zum Löschen einer Person aus dem Adressbuch
def person_loeschen(name):
    # Überprüfe, ob der Name im Adressbuch vorhanden ist
    if name in adressbuch:
        del adressbuch[name]  # Lösche den Eintrag
        print(f"{name} wurde aus dem Adressbuch gelöscht.")
    else:
        print(f"{name} wurde nicht gefunden.")


# Funktion zum Suchen der Kontaktdaten einer Person
def kontakt_suchen(name):
    # Überprüfe, ob der Name im Adressbuch vorhanden ist
    if name in adressbuch:
        # Hole Email und Telefonnummer aus dem Eintrag
        email = adressbuch[name]["Email"]
        telefonnummer = adressbuch[name]["Telefonnummer"]
        print(f"Kontaktdaten von {name}: Email: {email}, Telefonnummer: {telefonnummer}")
    else:
        print(f"{name} wurde nicht gefunden.")


# Funktion zum Aktualisieren der Informationen einer Person
def information_aktualisieren(name, email=None, telefonnummer=None):
    # Überprüfe, ob der Name im Adressbuch vorhanden ist
    if name in adressbuch:
        # Aktualisiere Email und/oder Telefonnummer, falls angegeben
        if email:
            adressbuch[name]["Email"] = email
        if telefonnummer:
            adressbuch[name]["Telefonnummer"] = telefonnummer
        print(f"Informationen von {name} wurden aktualisiert.")
    else:
        print(f"{name} wurde nicht gefunden.")


# Beispielverwendung der Funktionen
person_hinzufuegen("Alice", "alice@email.com", "0123456789")
person_loeschen("Bob")
kontakt_suchen("Alice")
information_aktualisieren("Alice", telefonnummer="9876543210")
