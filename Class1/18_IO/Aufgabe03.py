# Schreiben Sie ein Python-Skript, das alle Dateien in einem bestimmten Verzeichnis und in seinen Unterordnern
# durchsucht und alle Dateien findet, die eine bestimmte Zeichenfolge im Dateinamen enthalten. Das Verzeichnis und
# die zu suchende Zeichenfolge sollten als Parameter an das Skript übergeben werden.

import os


def find_files_with_string(directory, search_string):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if search_string in filename:
                matching_files.append(os.path.join(root, filename))
    return matching_files


# Beispielaufruf
directory = "./"
search_string = "hallo"
found_files = find_files_with_string(directory, search_string)
for file in found_files:
    print(file)
