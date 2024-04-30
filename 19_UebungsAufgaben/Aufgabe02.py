# Definieren Sie eine Basisklasse "Tier" mit Eigenschaften wie "name" und "alter". Leiten Sie zwei Unterklassen
# "Hund" und "Katze" von "Tier" ab, wobei jede Unterklasse zusätzliche Eigenschaften wie "rasse" für Hunde und
# "fellfarbe" für Katzen hat. Implementieren Sie eine Methode "beschreibe_tier()", die unterschiedliche Ausgaben für
# Hunde und Katzen generiert. Erstellen Sie Instanzen beider Klassen und demonstrieren Sie die Verwendung dieser
# Methode.

class Tier:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def beschreibe_tier(self):
        return f"{self.name} ist {self.alter} Jahre alt"


class Hund(Tier):
    def __init__(self, name, alter, rasse):
        super().__init__(name, alter)
        self.rasse = rasse

    def beschreibe_tier(self):
        return f"{super().beschreibe_tier()} und ist ein {self.rasse}"


class Katze(Tier):
    def __init__(self, name, alter, farbe):
        super().__init__(name, alter)
        self.farbe = farbe

    def beschreibe_tier(self):
        return f"{super().beschreibe_tier()} und ist {self.farbe}"


milu = Katze("Milu", 7, "schwarz weiss gefleckt")
print(milu.beschreibe_tier())

aimo = Hund("Aimo", 4, "Laggot")
print(aimo.beschreibe_tier())
