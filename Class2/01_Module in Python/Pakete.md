# Pakete

Ein Python-Paket ist ein Verzeichnis, das eine oder mehrere Python-Module enthält und eine spezielle Datei namens __init
__.py enthält. Es ermöglicht Ihnen, zusammengehörige Module in einer hierarchischen Verzeichnisstruktur zu organisieren
und sie als eigenständige Einheiten zu verwenden. Python-Pakete sind auch für die Veröffentlichung von Modulen über
Paketverwaltungstools wie pip oder setuptools geeignet.

---
Hier sind die Schritte, um ein Python-Paket zu erstellen:

### Schritt 1:

Verzeichnisstrukturen erstellen Sie ein Verzeichnis für Ihr Paket und legen Sie darin eine oder mehrere
Python-Moduldateien an. Das Verzeichnis kann auch Unterverzeichnisse enthalten, um Module in Unterpaketen zu
organisieren. Hier ist ein Beispiel für eine einfache Verzeichnisstruktur für ein Paket namens "mein_paket":

```
    mein_paket/
         __init__.py
         modul1.py
         modul2.py
         unterpaket/
         __init__.py
         modul3.py
 ```

---

### Schritt 2:

`__init__.py-Dateien` erstellen Jedes Verzeichnis im Paket sollte eine `__init__.py-Datei` enthalten. Diese Datei kann
leer sein oder Python-Code enthalten, der beim Import des Pakets oder Unterpakets ausgeführt wird. Sie kann auch als
Platzhalter für den Code dienen, der im Modul oder im Paket bereitgestellt wird. Hier ist ein Beispiel für eine `__init__
.py-Datei` für das oben gezeigte Paket:

 ```
    # Inhalt der __init__.py-Datei für mein_paket
    from . import modul1
    from . import modul2
    from .unterpaket import modul3
 ```

---

### Schritt 3:

Module in einem Paket verwenden Sie können nun auf die Module in Ihrem Paket zugreifen, indem Sie das Paket und den
Modulnamen in einem import-Befehl angeben. Hier ist ein Beispiel, wie Sie auf die Module in dem oben gezeigten "
mein_paket" zugreifen können:

 ```
    import mein_paket.modul1
    import mein_paket.modul2
    import mein_paket.unterpaket.modul3
    w
    # Verwendung der Module
    mein_paket.modul1.funktion1()
    mein_paket.modul2.funktion2()
    mein_paket.unterpaket.modul3.funktion3()
 ```

---

Alternativ können Sie auch einen import-Befehl mit dem from ... import ...-Syntax verwenden, um spezifische Funktionen,
Klassen oder Variablen aus den Modulen in das aktuelle Namensraum zu importieren:

 ```
    from mein_paket.modul1 import funktion1
    from mein_paket.modul2 import funktion2
    from mein_paket.unterpaket.modul3 import funktion3
    
    # Verwendung der Funktionen
    funktion1()
    funktion2()
    funktion3()
 ```

---