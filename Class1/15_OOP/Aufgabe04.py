class Mitarbeiter:
    def __init__(self, name, position, alter):
        self.name = name
        self.position = position
        self.alter = alter

    def __str__(self):
        return f"{self.name}, {self.position}, {self.alter}"


class Abteilung:
    def __init__(self, abteilungsname):
        self.abteilungsname = abteilungsname
        self.mitarbeiter_liste = []

    def mitarbeiter_hinzufuegen(self, mitarbeiter):
        self.mitarbeiter_liste.append(mitarbeiter)

    def mitarbeiter_auflisten(self):
        for mitarbeiter in self.mitarbeiter_liste:
            print(mitarbeiter)

    def mitarbeiter_durchschnittsalter(self):
        storage = 0
        for mitarbeiter in self.mitarbeiter_liste:
            storage += mitarbeiter.alter
        return storage / len(self.mitarbeiter_liste)


# Testaufrufe
# Erstellung von Mitarbeitern
mitarbeiter1 = Mitarbeiter("Max Mustermann", "Entwickler", 33)
mitarbeiter2 = Mitarbeiter("Erika Musterfrau", "Projektmanagerin", 27)

# Erstellung einer Abteilung und Hinzufügen von Mitarbeitern
abteilung = Abteilung("IT")
abteilung.mitarbeiter_hinzufuegen(mitarbeiter1)
abteilung.mitarbeiter_hinzufuegen(mitarbeiter2)

# Auflistung der Mitarbeiter in der Abteilung
abteilung.mitarbeiter_auflisten()

print(abteilung.mitarbeiter_durchschnittsalter())
