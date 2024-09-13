from dataclasses import dataclass, field
from typing import List
import json
from datetime import datetime


# Modell-Klassen definieren

@dataclass
class Kunde:
    name: str
    nummer: int


@dataclass
class Artikel:
    bezeichner: str
    nummer: int


@dataclass
class Position:
    nummer: int
    menge: int
    artikel: Artikel


@dataclass
class Lieferschein:
    nummer: int
    kunde: Kunde
    lieferDatum: str
    positionen: List[Position]


# Testdaten erstellen
kunde = Kunde(name="HFTM AG", nummer=5)

artikel1 = Artikel(bezeichner="HFTM Fan-Bag", nummer=1)
artikel2 = Artikel(bezeichner="HFTM Cap", nummer=2)

position1 = Position(nummer=1, menge=10, artikel=artikel1)
position2 = Position(nummer=2, menge=1, artikel=artikel2)

# Datum im gewünschten Format formatieren
lieferDatum = datetime.strptime("15.09.2022", "%d.%m.%Y").strftime("%d.%m.%Y")

lieferschein = Lieferschein(
    nummer=5,
    kunde=kunde,
    lieferDatum=lieferDatum,
    positionen=[position1, position2]
)

# Serialisierung nach JSON
json_result = json.dumps(lieferschein, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)

# Ausgabe des JSON
print(json_result)
