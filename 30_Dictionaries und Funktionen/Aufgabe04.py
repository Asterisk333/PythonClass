# Schreiben Sie ein Python-Programm, um ein neues Dictionary zu erstellen, indem Sie die genannten Schlüssel aus dem
# unten stehenden Dictionary extrahieren.
#
# sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# Zu extrahierende Keys
#
# keys = ["name", "salary"]
# Ergebnis:
# {'name': 'Kelly', 'salary': 8000}

def filter_dict(dict, keys):
    result = {}

    for key in keys:
        value = dict.get(key)
        result[key] = value

    return result


# ursprüngliches Dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

# Liste der Schlüssel
keys = ["name", "salary"]

print(filter_dict(sample_dict, keys))
