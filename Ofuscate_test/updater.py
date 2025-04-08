import os
import requests
import subprocess
import sys
import shutil

# Konfiguration
UPDATE_URL = "https://example.com/MeinProgramm.exe"  # Die URL zum neuesten Release
VERSION_URL = "https://example.com/version.txt"     # Version im Klartext, z. B. 1.0.0
CURRENT_VERSION = "1.0.0"                            # Die Version deiner aktuellen .exe
TEMP_UPDATE_PATH = "update.exe"                      # Temporärer Pfad für die neue .exe

def check_for_update():
    """Vergleicht die Version und prüft auf ein Update."""
    print("Prüfe auf Updates...")
    try:
        response = requests.get(VERSION_URL)
        latest_version = response.text.strip()
        if latest_version != CURRENT_VERSION:
            print(f"Neue Version gefunden: {latest_version}")
            download_and_replace(latest_version)
        else:
            print("Bereits die neueste Version!")
    except requests.RequestException as e:
        print(f"Fehler beim Überprüfen der Version: {e}")

def download_and_replace(latest_version):
    """Lädt die neue Version herunter und ersetzt die alte."""
    print("Lade die neueste Version herunter...")
    try:
        # Neue Version herunterladen
        response = requests.get(UPDATE_URL, stream=True)
        with open(TEMP_UPDATE_PATH, "wb") as f:
            shutil.copyfileobj(response.raw, f)
        print("Herunterladen abgeschlossen.")

        # Alte Version durch die neue ersetzen
        print("Ersetze die alte Version...")
        os.replace(TEMP_UPDATE_PATH, sys.executable)

        print(f"Die Version {latest_version} wurde erfolgreich installiert.")
        print("Starte die neue Version...")
        subprocess.run([sys.executable], check=True)  # Starte die neue Version
        sys.exit(0)  # Beende das alte Programm
    except requests.RequestException as e:
        print(f"Fehler beim Herunterladen des Updates: {e}")
    except Exception as e:
        print(f"Fehler beim Ersetzen der alten Version: {e}")

if __name__ == "__main__":
    check_for_update()
