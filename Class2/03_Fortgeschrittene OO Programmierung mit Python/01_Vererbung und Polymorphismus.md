Hier ist der Text in Markdown formatiert:

# Vererbung und Polymorphismus

Vererbung und Polymorphismus sind wichtige Konzepte in der objektorientierten Programmierung. Vererbung ermöglicht es einer Klasse, Eigenschaften und Methoden von einer anderen Klasse zu erben, während Polymorphismus es Objekten ermöglicht, unterschiedliche Formen oder Verhaltensweisen zu haben, je nachdem, welche Klasse sie instanziieren.

## Vererbung

Die Vererbung ermöglicht es, eine neue Klasse zu erstellen, die Eigenschaften und Methoden einer bestehenden Klasse erbt. Die neue Klasse wird als abgeleitete Klasse oder Subklasse bezeichnet, während die vorhandene Klasse als Basisklasse oder Superklasse bezeichnet wird.

Die Syntax für die Erstellung einer abgeleiteten Klasse in Python ist wie folgt:

```python
class SubklasseName(SuperklasseName):
    # Methoden und Eigenschaften der Subklasse
```

Die Subklasse erbt alle Methoden und Eigenschaften der Superklasse und kann auch eigene Methoden und Eigenschaften hinzufügen oder vorhandene überschreiben. Hier ist ein Beispiel:

```python
class Tier:
    def __init__(self, name):
        self.name = name

    def machen_laut(self):
        print("Das Tier macht einen Laut.")

class Hund(Tier):
    def machen_laut(self):
        print("Der Hund bellt.")

tier1 = Tier("Tier 1")
tier1.machen_laut()  # Ausgabe: Das Tier macht einen Laut.

hund1 = Hund("Hund 1")
hund1.machen_laut()  # Ausgabe: Der Hund bellt.
```

In diesem Beispiel hat die Klasse `Hund` die Klasse `Tier` als Basisklasse. Die Methode `machen_laut` der Klasse `Hund` überschreibt die Methode `machen_laut` der Klasse `Tier`. Wenn Sie `machen_laut` auf einem Tier-Objekt aufrufen, wird die `machen_laut`-Methode der `Tier`-Klasse ausgeführt, während die `machen_laut`-Methode der `Hund`-Klasse ausgeführt wird, wenn Sie sie auf einem Hund-Objekt aufrufen.

## Polymorphismus

Polymorphismus bezieht sich auf die Fähigkeit von Objekten, unterschiedliche Formen oder Verhaltensweisen zu haben, je nachdem, welche Klasse sie instanziieren. Es gibt zwei Arten von Polymorphismus: statischer Polymorphismus und dynamischer Polymorphismus.

- **Statischer Polymorphismus** bezieht sich auf die Überladung von Methoden mit unterschiedlichen Parametertypen oder -anzahlen.
- **Dynamischer Polymorphismus** bezieht sich auf die Verwendung von Polymorphismus bei der Vererbung.

Hier ist ein Beispiel für dynamischen Polymorphismus in Python:

```python
class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Ich bin eine Person und heiße", self.name)

class Student(Person):
    def __init__(self, name, matrikelnummer):
        super().__init__(name)
        self.matrikelnummer = matrikelnummer

    def info(self):
        print("Ich bin ein Student, heiße", self.name, "und habe die Matrikelnummer", self.matrikelnummer)
```

In diesem Beispiel haben wir zwei Klassen, `Person` und `Student`. `Student` erbt von `Person` und hat eine zusätzliche Eigenschaft `matrikelnummer`. Beide Klassen haben eine Methode `info`, aber `Student` überschreibt die `info`-Methode der `Person`-Klasse, um die Matrikelnummer in der Ausgabe zu zeigen.