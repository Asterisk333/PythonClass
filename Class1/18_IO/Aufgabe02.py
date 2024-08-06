# Schreiben Sie eine Python-Funktion, die den Inhalt einer JSON-Datei liest und eine Liste von Dictionaries
# zurückgibt, wobei jedes Dictionary einen Datensatz darstellt. Die JSON-Datei hat eine Liste von Objekten mit
# Schlüssel-Wert-Paaren.

import json


def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            if isinstance(data, list):
                return data
            else:
                print("Die JSON-Datei enthält keine Liste von Objekten.")
                return []
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
        return []


# Beispielaufruf
json_file_path = "test3.json"
records = read_json_file(json_file_path)
for record in records:
    print(record)
