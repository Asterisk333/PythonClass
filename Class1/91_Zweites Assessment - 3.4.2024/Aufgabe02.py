# Aufgabe 2:
# Definieren Sie eine Basisklasse Fahrzeug mit Eigenschaften wie marke, modell und baujahr. Leiten Sie
# zwei Unterklassen Auto und Motorrad von Fahrzeug ab, wobei jede Unterklasse eine zusätzliche, spezifische
# Eigenschaft hat (z.B. sitze für Autos und helmpflicht für Motorräder). Implementieren Sie eine Methode
# zeige_details(), die unterschiedliche Ausgaben für Auto und Motorrad generiert. Erstellen Sie Instanzen beider
# Klassen und demonstrieren Sie die Verwendung dieser Methode.

class Fahrzeug:
    def __init__(self, marke, modell, baujahr):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr

    def details_zeigen(self):
        return f"Marke: {self.marke}, Modell: {self.modell}, Baujahr: {self.baujahr}"


class Auto(Fahrzeug):
    def __init__(self, marke, modell, baujahr, sitze):
        super().__init__(marke, modell, baujahr)
        self.sitze = sitze

    def details_zeigen(self):
        return f"{super().details_zeigen()}, Sitze: {self.sitze}"


class Motorrad(Fahrzeug):
    def __init__(self, marke, modell, baujahr, helmpflicht):
        super().__init__(marke, modell, baujahr)
        self.helmpflicht = helmpflicht

    def details_zeigen(self):
        return f"{super().details_zeigen()}, Helmpflicht: {'ja' if self.helmpflicht else 'Nein'}"


auto = Auto("Tesla", "Model S", 2022, 5)
motorrad = Motorrad("Yamaha", "MT-07", 2021, True)

# Methode verwenden
print(auto.details_zeigen())
print(motorrad.details_zeigen())
