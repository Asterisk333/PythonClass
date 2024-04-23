# Schreiben Sie ein Python-Skript, das alle Dateien in einem bestimmten Verzeichnis und in seinen Unterordnern
# durchsucht und alle Dateien findet, die eine bestimmte Zeichenfolge im Dateinamen enthalten. Das Verzeichnis und
# die zu suchende Zeichenfolge sollten als Parameter an das Skript übergeben werden.

import os


def find_files_with_string(root_directory, search_string):
    matching_files = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if search_string in filename:
                matching_files.append(os.path.join(root, filename))
    return matching_files


# Beispielaufruf
verzeichnis = "./"
such_string = "hallo"
gefundene_dateien = find_files_with_string(verzeichnis, such_string)
for datei in gefundene_dateien:
    print(datei)
