# Schreiben Sie ein Python-Skript, das alle Textdateien in einem bestimmten Verzeichnis öffnet und die Anzahl der
# Vorkommnisse eines bestimmten Wortes in jeder Datei zählt. Das Wort und der Pfad zum Verzeichnis sollten als
# Parameter an die Funktion übergeben werden.

import os


def count_word_occurrences_in_files(directory_path, target_word):
    word_counts = {}
    # Durchsuche alle Dateien im Verzeichnis
    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                occurrences = content.lower().count(target_word.lower())
                word_counts[filename] = occurrences

    return word_counts


# Beispielaufruf
directory = "./"
word_to_count = "Python"
result = count_word_occurrences_in_files(directory, word_to_count)
for filename, count in result.items():
    print(f"{filename}: {count} Vorkommen von '{word_to_count}'")
