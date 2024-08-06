# Schreiben Sie ein Python-Programm, das den Inhalt einer CSV-Datei mit dem Namen "input.csv" in ein Dictionary liest
# und dann den Inhalt des Dictionaries in eine JSON-Datei namens "output.json" schreibt. Die CSV-Datei hat zwei
# Spalten: "name" und "alter". Das Dictionary sollte so aussehen: { "name1": alter1, "name2": alter2,
# ... }. Verwenden Sie die Module csv und json in Python, um diese Aufgabe zu lösen.

import csv
import json


def csv_to_dict(csv_file_path):
    data_dict = {}
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        # skip first row
        next(csv_reader)
        for row in csv_reader:
            name, age = row[0], row[1]
            data_dict[name] = int(age)
    return data_dict


def dict_to_json(data_dict, json_file_path):
    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(data_dict, jsonfile, ensure_ascii=False, indent=4)


csv_file_path = 'input.csv'
json_file_path = 'output.json'

data_dict = csv_to_dict(csv_file_path)

dict_to_json(data_dict, json_file_path)
