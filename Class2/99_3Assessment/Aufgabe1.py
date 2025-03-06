import json


produkte = {
    "Produkt1": {
        "Grundinformationen": {
            "Name": "Laptop",
            "Kategorie": "Elektronik",
            "Preis": 1200
        },
        "Details": {
            "Hersteller": "Dell",
            "Modell": "XPS 15",
            "Erscheinungsjahr": 2020
        },
        "Bewertungen": [4.5, 5, "sehr gut"]
    },
    "Produkt2": {
        "Grundinformationen": {
            "Name": "Kaffeemaschine",
            "Kategorie": "Haushalt",
            "Preis": 150
        },
        "Details": {
            "Hersteller": "Siemens",
            "Modell": "EQ.9",
            "Erscheinungsjahr": 2019
        },
        "Bewertungen": [4, 3.5, 4]
    }
}
with open("produkte.json", "w", encoding="utf-8") as f:
    json.dump(produkte, f, indent=4)
with open("produkte.json", "r", encoding="utf-8") as f:
    print(json.load(f))