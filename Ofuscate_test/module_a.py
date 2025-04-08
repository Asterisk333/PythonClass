import os
import sys


def resource_path(relative_path):
    """Ermittle den absoluten Pfad zu einer Ressource,
       egal ob im Entwicklungsmodus oder als gepackte EXE.
    """
    try:
        # Falls gepackte EXE: sys._MEIPASS enthält das temporäre Verzeichnis
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)