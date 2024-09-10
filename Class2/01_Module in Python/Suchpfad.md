# Suchpfad

Der Modulsuchpfad in Python ist eine Liste von Verzeichnissen, in denen Python nach Modulen sucht, wenn sie mit dem
import-Befehl geladen werden. Die Reihenfolge der Verzeichnisse im Suchpfad ist wichtig, da Python die Module in der
Reihenfolge sucht, in der sie aufgeführt sind, und das erste gefundene Modul verwendet.

Der Modulsuchpfad in Python kann durch das sys-Modul abgerufen und bearbeitet werden. Hier ist ein Beispiel, wie Sie auf
den Modulsuchpfad zugreifen können:

```
    import sys
    
    # Abrufen des aktuellen Modulsuchpfads
    
    module_search_path = sys.path
    print("Modulsuchpfad:", module_search_path)
    
    # Hinzufügen eines Verzeichnisses zum Modulsuchpfad
    
    new_path = "/pfad/zum/verzeichnis"
    sys.path.append(new_path)
    print("Modulsuchpfad nach Hinzufügen:", sys.path)
    
    # Löschen eines Verzeichnisses aus dem Modulsuchpfad
    
    sys.path.remove(new_path)
    print("Modulsuchpfad nach Löschen:", sys.path)
```

Standardmäßig enthält der Modulsuchpfad die Pfade des aktuellen Verzeichnisses (in dem das ausführbare Skript oder die
Python-Interaktive Umgebung gestartet wurde), die in der Umgebungsvariable PYTHONPATH festgelegten Pfade und die
Standardbibliothekspfade von Python. Sie können Verzeichnisse zum Modulsuchpfad hinzufügen oder daraus entfernen, um die
Suche nach Modulen anzupassen, insbesondere wenn Sie eigene Module erstellen oder externe Bibliotheken verwenden, die
nicht im Standardmodulsuchpfad enthalten sind.

---