# Einführung

## Einleitung

Module werden verwendet, um größere Python-Projekte zu organisieren. Die Python-Standardbibliothek ist in Module
aufgeteilt, um sie überschaubarer zu machen. Sie müssen Ihren eigenen Code nicht in Modulen organisieren, aber wenn Sie
Programme schreiben, die mehr als ein paar Seiten lang sind, oder Code, den Sie wiederverwenden möchten, sollten Sie
dies tun.

### Was sind Module

In Python sind Module einfach Dateien mit Python-Code, die Funktionen, Klassen oder Variablen enthalten, die in anderen
Python-Programmen wiederverwendet werden können. Module ermöglichen die Organisation von Code in separaten Dateien, um
die Wartbarkeit und Wiederverwendbarkeit von `Python-Programmen zu verbessern.`

--- 

### Erstellen eines Moduls:

Ein Modul wird in Python durch Erstellen einer Datei mit der Erweiterung ".py" erstellt. Jede Funktion, Klasse oder
Variable, die Sie in anderen Python-Programmen wiederverwenden möchten, kann in einem Modul definiert werden. Hier ist
ein einfaches Beispiel für ein Python-Modul namens "example_module.py", das eine Funktion und eine Variable enthält:

```
    # Beispiel für ein Python-Modul
    # Eine Beispiel-Funktion
    
    def greet(name):
        print("Hallo, " + name + "!")
        
        # Eine Beispiel-Variable
        
        my_variable = 42
```

---

### Verwenden eines Moduls:

Nachdem Sie ein Modul erstellt haben, können Sie es in anderen Python-Programmen verwenden, indem Sie es importieren.
Verwenden Sie dazu das Schlüsselwort "import" gefolgt vom Modulnamen ohne die ".py"-Erweiterung. Hier ist ein Beispiel
für die Verwendung des oben erstellten Moduls "example_module" in einem anderen Python-Programm:

```
    # Beispiel für die Verwendung eines Moduls in Python
    # Importieren des Moduls
    
    import example_module
    
    # Verwendung der Funktion aus dem Modul
    
    example_module.greet("Alice")
        # Verwendung der Variable aus dem Modul
        
        print(example_module.my_variable)
```

Sie können auch bestimmte Funktionen, Klassen oder Variablen aus einem Modul importieren, anstatt das gesamte Modul zu
importieren. Hier ist ein Beispiel:

```
    # Beispiel für die Verwendung bestimmter Elemente aus einem Modul
    # Importieren der Funktion und Variable aus dem Modul
    
    from example_module import greet, my_variable
        # Verwendung der importierten Funktion und Variable
        
        greet("Bob")
        print(my_variable)
```

---

### Erstellen von eigenen Modulen:

Sie können auch Ihre eigenen Module erstellen, indem Sie Funktionen, Klassen oder Variablen in einer separaten Datei
organisieren und diese Datei dann in anderen Python-Programmen importieren. Hier ist ein einfaches Beispiel für ein
eigenes Modul "my_module.py":

```
    # Beispiel für ein eigenes Python-Modul
    # Eine Funktion im Modul
    
    def add_numbers(a, b):
        return a + b
 ```

---

### Verwenden von Modulen aus Standardbibliotheken

Python bietet eine Vielzahl von Standardbibliotheken, die viele nützliche Module enthalten, die in Ihren Programmen
verwendet werden können. Sie können diese Module einfach importieren und verwenden. Hier ist ein Beispiel für die
Verwendung des "random"-Moduls aus der Python-Standardbibliothek:

```
    # Beispiel für die Verwendung des "random"-Moduls aus der Python-Standardbibliothek
    # Importieren des "random"-Moduls
    
    import random
    # Verwendung von Funktionen aus dem "random"-Modul
    
    random_number = random.randint(1, 10)
    print("Zufällige Zahl:", random_number)
```

---