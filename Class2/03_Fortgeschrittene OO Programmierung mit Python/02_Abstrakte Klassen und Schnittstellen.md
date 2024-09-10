Hier ist der Text in Markdown formatiert:

# Abstrakte Klassen und Schnittstellen in Python

In der objektorientierten Programmierung bezieht sich eine **Schnittstelle** auf eine Zusammenstellung von Methoden, die von einem Objekt bereitgestellt werden. Eine Klasse kann eine Schnittstelle implementieren, indem sie eine Reihe von Methoden bereitstellt, die von anderen Klassen implementiert werden müssen. Eine **abstrakte Klasse** ist eine Klasse, die eine oder mehrere abstrakte Methoden enthält, für die keine Implementierung bereitgestellt wird.

## Abstrakte Klassen in Python

Eine abstrakte Klasse ist eine Klasse, die mindestens eine abstrakte Methode enthält. Eine abstrakte Methode ist eine Methode, die in der abstrakten Klasse definiert ist, aber keine Implementierung enthält. Stattdessen müssen Unterklassen der abstrakten Klasse die abstrakte Methode implementieren. In Python können wir abstrakte Klassen mit Hilfe des Moduls `abc` (Abstract Base Classes) definieren.

Hier ist ein Beispiel für eine abstrakte Klasse in Python:

```python
from abc import ABC, abstractmethod

class Form(ABC):
    @abstractmethod
    def berechne_fläche(self):
        pass

class Rechteck(Form):
    def __init__(self, länge, breite):
        self.länge = länge
        self.breite = breite

    def berechne_fläche(self):
        return self.länge * self.breite

class Kreis(Form):
    def __init__(self, radius):
        self.radius = radius

    def berechne_fläche(self):
        return 3.14 * self.radius ** 2
```

In diesem Beispiel haben wir die abstrakte Klasse `Form` definiert, die eine abstrakte Methode `berechne_fläche` enthält. Wir haben dann zwei Unterklassen `Rechteck` und `Kreis` erstellt, die von `Form` erben. Jede der Unterklassen implementiert die Methode `berechne_fläche` auf ihre eigene Weise.

Beachten Sie, dass wir die `abstractmethod`-Dekoratorfunktion verwenden, um die `berechne_fläche`-Methode als abstrakt zu markieren. Wenn eine Klasse eine abstrakte Methode enthält, kann sie **nicht direkt instanziiert werden**. Stattdessen muss eine konkrete Unterklasse erstellt werden, die die abstrakte Methode implementiert.

## Schnittstellen in Python

Eine **Schnittstelle** ist eine Klasse oder ein Datentyp, der eine Sammlung von Methoden und Attributen definiert, die von anderen Klassen oder Datentypen implementiert werden müssen. In Python können wir Schnittstellen ebenfalls mit Hilfe des Moduls `abc` (Abstract Base Classes) definieren.

**Wichtig:** Abstrakte Klassen dürfen auch konkrete Methoden haben!

Hier ist ein Beispiel für eine Schnittstelle in Python:

```python
from abc import ABC, abstractmethod

class Datenbank(ABC):
    @abstractmethod
    def verbinde(self):
        pass

    @abstractmethod
    def lese_daten(self, query):
        pass

    @abstractmethod
    def schreibe_daten(self, query, daten):
        pass

class MySQLDatenbank(Datenbank):
    def verbinde(self):
        # Verbindung zur MySQL-Datenbank herstellen
        pass

    def lese_daten(self, query):
        # Daten aus MySQL lesen
        pass

    def schreibe_daten(self, query, daten):
        # Daten in MySQL schreiben
        pass
```

In diesem Beispiel haben wir eine Schnittstelle `Datenbank` definiert, die drei abstrakte Methoden enthält: `verbinde`, `lese_daten` und `schreibe_daten`. Die Klasse `MySQLDatenbank` implementiert diese Methoden und stellt die Logik für den Zugriff auf eine MySQL-Datenbank bereit.