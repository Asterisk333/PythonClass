# Aufgabe 2: Abstrakte Klassen und Schnittstellen
# Aufgabe für abstrakte Klassen: Erstellen Sie eine abstrakte Klasse "Fahrzeug" mit der abstrakten Methode "fahren()".
# Erstellen Sie dann die beiden Unterklassen "Auto" und "Fahrrad", die von "Fahrzeug" erben. Implementieren Sie die
# Methode "fahren()" in jeder Unterklasse, um das jeweilige Fahrzeugtypspezifische Verhalten zu modellieren. Erstellen
# Sie zum Schluss eine Instanz jedes Objekts und rufen Sie die Methode "fahren()" auf, um zu überprüfen, ob sie wie
# erwartet funktioniert.
#
# Aufgabe für Schnittstellen: Erstellen Sie eine Schnittstelle "KannSprechen" mit der Methode "sprechen()". Erstellen
# Sie dann eine Klasse "Hund" und eine Klasse "Mensch", die die Schnittstelle "KannSprechen" implementieren.
# Implementieren Sie die Methode "sprechen()" in jeder Klasse auf eine Weise, die das charakteristische Sprechverhalten
# des jeweiligen Wesens widerspiegelt. Erstellen Sie zum Schluss eine Instanz jeder Klasse und rufen Sie die Methode
# "sprechen()" auf, um zu überprüfen, ob sie wie erwartet funktioniert.

from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    @abstractmethod
    def fahren(self):
        pass


class Auto(Fahrzeug):
    def fahren(self):
        return "Faehrt auf der Strasse"


class Fahrrad(Fahrzeug):
    def fahren(self):
        return "Faehrt auf dem Fahrrad-streifen"


# Beispielverwendung
auto = Auto()
fahrrad = Fahrrad()

print(auto.fahren())  # Ausgabe: Faehrt auf der Strasse.
print(fahrrad.fahren())  # Ausgabe: Faehrt auf dem Fahrrad-streifen.


print("--------------------------")


class KannSprechen(ABC):
    @abstractmethod
    def sprechen(self):
        pass


class Hund(KannSprechen):
    def sprechen(self):
        return "Der Hund bellt."


class Mensch(KannSprechen):
    def sprechen(self):
        return "Der Mensch spricht."


# Beispielverwendung
hund = Hund()
mensch = Mensch()

print(hund.sprechen())  # Ausgabe: Der Hund bellt.
print(mensch.sprechen())  # Ausgabe: Der Mensch spricht.
