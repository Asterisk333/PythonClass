# Aufgabe 1: Datenbankzugriff – Speichern von Daten
# Gegeben:
# Eine Klasse `DatabaseHandler`, die eine Methode `save_record` hat, um Datensätze in einer Datenbank zu speichern.

# Schritte: 1. Erstelle eine Klasse `DatabaseHandler` mit der Methode `save_record`. 2. Simuliere in einer Testklasse
# `TestDatabaseHandler`, dass die Methode `save_record` eine Datenbankoperation durchführt. 3. Verwende `MagicMock`,
# um die Methode `save_record` so zu simulieren, dass sie bei erfolgreicher Ausführung `True` zurückgibt. 4.
# Überprüfe in deinem Test, ob `save_record` aufgerufen wurde und ob das Rückgabeverhalten korrekt ist.

# Import der benötigten Module
from unittest import TestCase
from unittest.mock import MagicMock


# Klasse zur Verwaltung der Datenbankoperationen
class DatabaseHandler:
    def save_record(self, record):
        """
        Simuliert das Speichern eines Datensatzes in einer Datenbank.
        In einer echten Implementierung würde hier die Datenbanklogik stehen.
        """
        pass  # Hier würde die eigentliche Datenbankoperation durchgeführt werden


# Testklasse für DatabaseHandler
class TestDatabaseHandler(TestCase):
    def test_save_record_success(self):
        # Instanz der DatabaseHandler-Klasse
        db_handler = DatabaseHandler()

        # Erstelle eine MagicMock-Instanz für die save_record Methode
        db_handler.save_record = MagicMock(return_value=True)

        # Simulierter Datensatz
        record = {"id": 1, "name": "John Doe"}

        # Teste, ob save_record True zurückgibt
        result = db_handler.save_record(record)

        # Überprüfen, ob die Methode save_record aufgerufen wurde
        db_handler.save_record.assert_called_once_with(record)

        # Überprüfen, ob das Rückgabeverhalten korrekt ist
        self.assertTrue(result)


if __name__ == '__main__':
    TestDatabaseHandler.main()
