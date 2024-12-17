import json

# JSON-Datei öffnen und einlesen
with open('students.json', 'r') as file:
    data = json.load(file)

# Namen und Noten aller Studenten ausgeben
print("Namen und Noten aller Studenten:")
for student in data['students']:
    print(f"- {student['name']}: {student['grade']}")

# Alter des letzten Studenten erhöhen
data['students'][-1]['age'] += 1

# Änderungen in der JSON-Datei speichern
with open('students.json', 'w') as file:
    json.dump(data, file, indent=4)

print("\nDas Alter des letzten Studenten wurde um 1 erhöht.")
