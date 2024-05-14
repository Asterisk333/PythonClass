# Schreiben Sie eine Python-Funktion, die den Pfad zu einem Verzeichnis als Parameter erhält und eine Liste aller
# Dateien im Verzeichnis zurückgibt, die die Dateierweiterung ".jpg" haben.

import os


def find_jpg_files(directory_path):
    jpg_files = []

    if os.path.isdir(directory_path):
        for file in os.listdir(directory_path):
            if file.endswith('.jpg'):
                jpg_files.append(file)
    else:
        print(f"Der angegebene Pfad {directory_path} ist kein Verzeichnis.")

    return jpg_files


directory_path = './Bilder'
jpg_files_list = find_jpg_files(directory_path)
print(jpg_files_list)
