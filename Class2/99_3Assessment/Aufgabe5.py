import json
import pandas as pd
import xml.etree.ElementTree as ET

with open("produkte.json", "r", encoding="utf-8") as f:
    produkte = json.load(f)
df_produkte = pd.json_normalize(produkte, sep="_")

# CSV-Daten laden
df_csv = pd.read_csv("produkte.csv")

# XML-Daten laden
tree = ET.parse("filme.xml")
root = tree.getroot()
filme_liste = []

for film in root.findall("film"):
    filme_liste.append({
        "genre": film.attrib.get("genre"),
        "dauer": int(film.attrib.get("dauer")),
        "erscheinungsjahr": int(film.find("erscheinungsjahr").text)
    })
df_filme = pd.DataFrame(filme_liste)



print(df_csv)
print(df_filme)
print(df_produkte)