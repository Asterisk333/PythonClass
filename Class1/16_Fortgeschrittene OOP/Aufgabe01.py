class Fahrzeug:
    def __init__(self, kapazitaet):
        self.kapazitaet = kapazitaet

    def berechne_tarif(self):
        return self.kapazitaet * 100


class Bus(Fahrzeug):
    def berechne_tarif(self):
        standard_tarif = super().berechne_tarif()
        wartungsgebuehr = standard_tarif * 0.10
        return standard_tarif + wartungsgebuehr


# Beispiel
bus = Bus(50)  # Angenommen, der Bus hat 50 Sitzplätze
print(f"Der Gesamtfahrpreis für die Bus-Instanz ist: {bus.berechne_tarif()} CHF")
