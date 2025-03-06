import xml.etree.ElementTree as ET

tree = ET.parse("filme.xml")
root = tree.getroot()
filme_liste = []

for film in root.findall("film"):
    daten = {
        "titel": film.find("titel").text,
        "regisseur": film.find("regisseur").text,
        "erscheinungsjahr": film.find("erscheinungsjahr").text,
        "genre": film.attrib.get("genre"),
        "dauer": film.attrib.get("dauer")
    }
    filme_liste.append(daten)
    print(
        f"Film gefunden: Titel={daten['titel']}, Regisseur={daten['regisseur']}, Erscheinungsjahr={daten['erscheinungsjahr']}, Genre={daten['genre']}, Dauer={daten['dauer']}")

print("\nListe von Dictionaries:")
print(filme_liste)
