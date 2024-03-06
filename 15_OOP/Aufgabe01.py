# Eine Fahrzeugklasse definieren
class Vehicle:
    # Ein Konstruktor mit zwei Instanzattributen: max_speed und mileage
    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage

    # Eine Methode, um die Fahrzeuginformationen auszugeben
    def display_info(self):
        print(
            f"Dieses Fahrzeug hat eine maximale Geschwindigkeit von {self.max_speed} km/h und eine Laufleistung von {self.mileage} km.")


# Ein Objekt der Fahrzeugklasse erstellen
car = Vehicle(200, 15000)

# Die Fahrzeuginformationen anzeigen
car.display_info()
