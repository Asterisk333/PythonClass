# Adressbuch Programm Implementiere ein einfaches Adressbuch mit Python, das Dictionaries verwendet. Jeder Eintrag im
# Adressbuch soll den Namen einer Person (als Schlüssel) und weitere Informationen wie E-Mail und Telefonnummer (als
# Dictionary) enthalten. Das Programm soll folgende Funktionen haben:

# einer neuen Person zum Adressbuch.
# Löschen einer Person aus dem Adressbuch.
# Suchen der Kontaktdaten (E-Mail, Telefonnummer) einer Person.
# Bonus: Füge die Möglichkeit hinzu, die Informationen einer Person zu aktualisieren.

# Initialisiere ein leeres Dictionary für das Adressbuch
class Adressbuch:
    def __init__(self):
        self.adressbuch = {}

    # Funktion zum Hinzufügen einer neuen Person zum Adressbuch
    def person_hinzufuegen(self, name, email, telefonnummer):
        # Überprüfe, ob der Name bereits ein Schlüssel im Adressbuch ist
        if name not in self.adressbuch:
            # Erstelle einen neuen Eintrag mit Email und Telefonnummer
            self.adressbuch[name] = {"Email": email, "Telefonnummer": telefonnummer}
            print(f"{name} wurde zum Adressbuch hinzugefügt.")
        else:
            print(f"{name} ist bereits im Adressbuch.")

    # Funktion zum Löschen einer Person aus dem Adressbuch
    def person_loeschen(self, name):
        # Überprüfe, ob der Name im Adressbuch vorhanden ist
        if name in self.adressbuch:
            del self.adressbuch[name]  # Lösche den Eintrag
            print(f"{name} wurde aus dem Adressbuch gelöscht.")
        else:
            print(f"{name} wurde nicht gefunden.")

    # Funktion zum Suchen der Kontaktdaten einer Person
    def kontakt_suchen(self, name):
        # Überprüfe, ob der Name im Adressbuch vorhanden ist
        if name in self.adressbuch:
            # Hole Email und Telefonnummer aus dem Eintrag
            email = self.adressbuch[name]["Email"]
            telefonnummer = self.adressbuch[name]["Telefonnummer"]
            print(f"Kontaktdaten von {name}: Email: {email}, Telefonnummer: {telefonnummer}")
        else:
            print(f"{name} wurde nicht gefunden.")

    # Funktion zum Aktualisieren der Informationen einer Person
    def information_aktualisieren(self, name, email=None, telefonnummer=None):
        # Überprüfe, ob der Name im Adressbuch vorhanden ist
        if name in self.adressbuch:
            # Aktualisiere Email und/oder Telefonnummer, falls angegeben
            if email:
                self.adressbuch[name]["Email"] = email
            if telefonnummer:
                self.adressbuch[name]["Telefonnummer"] = telefonnummer
            print(f"Informationen von {name} wurden aktualisiert.")
        else:
            print(f"{name} wurde nicht gefunden.")


# Beispielverwendung der Funktionen

adressbuch = Adressbuch()
adressbuch.person_hinzufuegen("Alice", "alice@email.com", "0123456789")
adressbuch.person_loeschen("Bob")
adressbuch.kontakt_suchen("Alice")
adressbuch.kontakt_suchen("Alice")
