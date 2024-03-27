# Aufgabe 3: Bibliothekssystem
# Entwickle ein einfaches Bibliothekssystem, das objektorientierte Programmierung nutzt.
# Dein System soll zwei Hauptklassen haben: Buch und Bibliothek.

# Klasse Buch: Attribute: titel (String), autor (String), isbn (String). Der Konstruktor (__init__ Methode) sollte
# diese Attribute initialisieren. Füge eine Methode info hinzu, die eine formatierte Zeichenkette mit Informationen
# über das Buch zurückgibt (z.B. "Titel: [Titel], Autor: [Autor], ISBN: [ISBN]"). klasse Bibliothek: attribute: name
# (String), bestand (Liste von Buch-Objekten). methoden: buch_hinzufuegen(buch): Nimmt ein Buch-Objekt entgegen und
# fügt es zum Bestand hinzu. Überprüfe, ob das Buch bereits existiert (basierend auf ISBN), und füge es nur hinzu,
# wenn es neu ist. buch_entfernen(isbn): Entfernt ein Buch anhand seiner ISBN aus dem Bestand. suche_nach_titel(
# titel): Gibt eine Liste von Büchern zurück, die den gegebenen Titel enthalten. Nutze hierfür eine Schleife,
# um durch den Bestand zu iterieren. anzeigen_aller_buecher(): Druckt Informationen zu allen Büchern in der
# Bibliothek aus. Verwende die info Methode der Buch-Klasse.

class Buch:
    # Der Konstruktor der Klasse Buch, der beim Erstellen eines neuen Buch-Objekts aufgerufen wird.
    def __init__(self, titel, autor, isbn):
        # Initialisiere die Attribute des Buches mit den übergebenen Parametern.
        self.titel = titel
        self.autor = autor
        self.isbn = isbn

    # Methode, um eine formatierte Zeichenkette mit Informationen über das Buch zurückzugeben.
    def info(self):
        # Gibt die Buchinformationen als formatierten String zurück.
        return f"Titel: {self.titel}, Autor: {self.autor}, ISBN: {self.isbn}"


class Bibliothek:
    # Der Konstruktor der Klasse Bibliothek, der beim Erstellen eines neuen Bibliothek-Objekts aufgerufen wird.
    def __init__(self, name):
        # Initialisiere die Attribute der Bibliothek.
        self.name = name  # Der Name der Bibliothek.
        self.bestand = []  # Eine Liste, die die Buch-Objekte enthält.

    # Methode zum Hinzufügen eines Buches zum Bestand der Bibliothek.
    def buch_hinzufuegen(self, buch):
        # Durchlaufe den Bestand, um zu überprüfen, ob das Buch bereits vorhanden ist.
        for vorhandenes_buch in self.bestand:
            if vorhandenes_buch.isbn == buch.isbn:
                # Wenn das Buch bereits existiert, gebe eine Nachricht aus und beende die Funktion.
                print(f"Das Buch mit der ISBN {buch.isbn} existiert bereits im Bestand.")
                return
        # Wenn das Buch nicht vorhanden ist, füge es zum Bestand hinzu.
        self.bestand.append(buch)
        print(f"Das Buch '{buch.titel}' wurde zum Bestand hinzugefügt.")

    # Methode zum Entfernen eines Buches aus dem Bestand der Bibliothek anhand seiner ISBN.
    def buch_entfernen(self, isbn):
        # Durchlaufe den Bestand, um das Buch mit der gegebenen ISBN zu finden.
        for buch in self.bestand:
            if buch.isbn == isbn:
                # Wenn das Buch gefunden wird, entferne es aus dem Bestand.
                self.bestand.remove(buch)
                print(f"Das Buch mit der ISBN {isbn} wurde aus dem Bestand entfernt.")
                return
        # Wenn das Buch nicht gefunden wird, gebe eine Nachricht aus.
        print(f"Ein Buch mit der ISBN {isbn} wurde nicht gefunden.")

    # Methode zum Suchen von Büchern im Bestand anhand ihres Titels.
    def suche_nach_titel(self, titel):
        # Erstelle eine Liste von Büchern, deren Titel den gesuchten Titel enthalten.
        for buch in [buch for buch in self.bestand if titel.lower() in buch.titel.lower()]:
            print(buch.info())

    # Methode zum Anzeigen aller Bücher im Bestand der Bibliothek.
    def anzeigen_aller_buecher(self):
        # Durchlaufe den Bestand und verwende die info-Methode jedes Buches, um seine Informationen auszugeben.
        for buch in self.bestand:
            print(buch.info())


# Beispielverwendung
bibliothek = Bibliothek("Stadtbibliothek Solothurn")  # Erstelle ein neues Bibliothek-Objekt.
dasKapital = Buch("Das Kapital", "Karl Marx", "978-3-16-148410-0")  # Erstelle ein neues Buch-Objekt.
gatsby = Buch("Der große Gatsby", "F. Scott Fitzgerald", "978-3-12-579850-2")  # Erstelle ein weiteres Buch-Objekt.

# Füge die Bücher zum Bestand der Bibliothek hinzu.
bibliothek.buch_hinzufuegen(dasKapital)
bibliothek.buch_hinzufuegen(gatsby)
# Zeige alle Bücher in der Bibliothek an.
bibliothek.anzeigen_aller_buecher()

# Suche nach einem Buchtitel und zeige die gefundenen Bücher an.
bibliothek.suche_nach_titel("kapital")

# Entferne ein Buch mit einer bestimmten ISBN und zeige den aktualisierten Bestand an.
bibliothek.buch_entfernen("978-3-16-148410-0")
bibliothek.anzeigen_aller_buecher()
