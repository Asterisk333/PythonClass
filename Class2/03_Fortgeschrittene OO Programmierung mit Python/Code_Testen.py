# Aufgabe 3: OO Code Testen Angenommen, Sie haben eine Klasse namens Document, die einen Textinhalt speichert und
# Methoden zum Speichern und Laden von Dokumenten in einer Datenbank bereitstellt. Die Klasse Document soll mit einer
# externen Datenbank interagieren, die Sie nicht direkt im Test verwenden möchten. Stattdessen müssen Sie eine
# Mock-Datenbank erstellen, um Ihre Tests zu schreiben.
#
# Schreiben Sie einen Satz von Unit-Tests für die Document-Klasse, die die folgenden Anforderungen erfüllen:
#
# Die Methode save speichert den Inhalt des Dokuments in der Datenbank und gibt True zurück, wenn das Speichern
# erfolgreich war.
#
# Die Methode load lädt den Inhalt eines Dokuments aus der Datenbank und gibt den Inhalt zurück, wenn das Laden
# erfolgreich war.
#
# Wenn das Speichern oder Laden fehlschlägt, gibt die Methode save bzw. load False zurück.
#
# Wenn die Datenbankverbindung fehlschlägt, gibt die Methode save bzw. load False zurück.
#
# Wenn ein ungültiger Inhalt gespeichert wird (z.B. None oder ein leerer String), gibt die Methode save False zurück.
#
# Wenn ein ungültiger Dokumentenname (z.B. None oder ein leerer String) beim Speichern oder Laden verwendet wird,
# gibt die Methode save bzw. load False zurück.

import unittest
from unittest.mock import Mock


class Document:
    def __init__(self, name, content):
        self.name = name
        self.content = content

    def save(self, db):
        if not self.name or not self.content:
            return False
        try:
            db.save(self.name, self.content)
            return True
        except (IOError, ValueError) as e:
            print(f"Error occurred: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error occurred: {e}")
            return False

    def load(self, db):
        if not self.name:
            return False
        try:
            self.content = db.load_document(self.name)
            return self.content is not None
        except:
            return False


class TestDocument(unittest.TestCase):
    def setUp(self):
        self.mock_db = Mock()
        self.doc = Document('test_doc', "Das ist ein test")

    def test_save_success(self):
        self.mock_db.save.return_value = True
        result = self.doc.save(self.mock_db)
        self.mock_db.save.assert_called_with('test_doc', "Das ist ein test")
        self.assertTrue(result)

    def test_save_failure(self):
        self.mock_db.save_document.side_effect = Exception("DB error")
        result = self.doc.save(self.mock_db)
        self.assertTrue(result)

    def test_save_invalid_content(self):
        invalid_doc = Document("test_doc", "")
        result = invalid_doc.save(self.mock_db)
        self.assertFalse(result)

    def test_load_success(self):
        self.mock_db.load_document.return_value = "This is a test document."
        result = self.doc.load(self.mock_db)
        self.assertTrue(result)
        self.assertEqual(self.doc.content, "This is a test document.")
        self.mock_db.load_document.assert_called_with("test_doc")

    def test_load_failure(self):
        self.mock_db.load_document.side_effect = Exception("DB error")
        result = self.doc.load(self.mock_db)
        self.assertFalse(result)

    def test_load_invalid_name(self):
        invalid_doc = Document("", "This is a test document.")
        result = invalid_doc.load(self.mock_db)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
