import json

# JSON-Datei öffnen und einlesen
with open('books.json', 'r') as file:
    data = json.load(file)

# Titel aller Bücher ausgeben
print("Titel aller Bücher:")
for book in data['books']:
    print(f"- {book['title']}")

# Jahr des ersten Buches ändern
data['books'][0]['year'] = 2021

# Änderungen in der JSON-Datei speichern
with open('books.json', 'w') as file:
    json.dump(data, file, indent=4)

print("\nDas Jahr des ersten Buches wurde geändert.")

