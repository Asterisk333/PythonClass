### Projektziel:
Das Ziel des Projekts besteht darin, ein XML-Dokument in eine JSON-Struktur zu überführen, um die Informationen in 
einem modernen und weit verbreiteten Datenformat verfügbar zu machen. Besonders wichtig ist die Validierung des
XML-Dokuments, um sicherzustellen, dass nur gültige Daten verarbeitet werden.

### Projektbeschreibung:
Das Programm liest ein XML-Dokument mithilfe von ElementTree ein, validiert es und überführt es in eine 
objektorientierte Struktur. Anschließend wird der Inhalt als JSON-Datei exportiert. Das Programm kann über die 
Kommandozeile gestartet werden und ermöglicht es dem Benutzer, das zu verarbeitende XML-Dokument auszuwählen.

### Reflexion:
Beim Implementieren stellte sich heraus, dass die Validierung des XML-Dokuments gegen das Schema einige 
Schwierigkeiten bereitete, insbesondere bei der Handhabung von optionalen Attributen. Ich habe gelernt, wie man 
XML-Schemas effizient einsetzt und wie man komplexere JSON-Strukturen mit Python erstellt.


### Erklärung des Codes:

1. **XML-Validierung**:
   - Die Funktion `validate_xml()` prüft, ob das XML-Dokument gegenüber dem angegebenen Schema gültig ist.
   - Dazu wird die Bibliothek **lxml** verwendet, um das XML-Schema (`XSD`) zu validieren.
   - Nur wenn das Dokument gültig ist, wird die Verarbeitung fortgesetzt.

2. **Objektorientierte Abbildung**:
   - Die Klassen `Product` und `ProductList` repräsentieren die Produkte und deren Sammlung.
     - Die Klasse `Product` enthält Attribute wie `product_id`, `name`, `price`, `category` und `stock`.
     - Die Methode `to_dict()` wandelt ein `Product`-Objekt in ein Dictionary um, das später für den JSON-Export 
     verwendet wird.
   - `ProductList` speichert eine Liste von Produkten und bietet eine Methode `to_dict()`, die eine Liste von 
   Produkt-Dictionaries zurückgibt.

3. **Parsing des XML**:
   - Die Funktion `parse_xml()` liest das XML-Dokument mit der Bibliothek **ElementTree** ein und sucht nach den 
   einzelnen `product`-Elementen.
   - Jedes `product`-Element wird zu einem `Product`-Objekt umgewandelt, indem die Attribute wie `name`, `price`, 
   `category` und `stock` extrahiert werden.
   - Die erstellten `Product`-Objekte werden in der `ProductList` gespeichert.

4. **JSON-Export**:
   - Die Funktion `export_to_json()` nimmt die Liste der Produkte (in Dictionary-Form) und speichert sie als JSON-Datei.
   - Das Python-Modul **json** wird verwendet, um die Daten in das JSON-Format umzuwandeln und in eine Datei zu 
   schreiben.
   - Die Option `indent=4` sorgt dafür, dass die JSON-Daten gut lesbar formatiert sind.

5. **Main-Funktion**:
   - Die `main()`-Funktion ist der Hauptprogrammablauf.
   - Zuerst wird das XML-Dokument mit dem XML-Schema validiert.
   - Ist die Validierung erfolgreich, werden die Daten aus dem XML-Dokument geparst und in Python-Objekte überführt.
   - Anschließend werden die Daten in einer JSON-Datei gespeichert.
   - Die Datei wird unter dem angegebenen Dateinamen exportiert.

### Beispielhafter Ablauf:
1. Das Programm wird mit einem XML-Dokument (`products.xml`) und einem XML-Schema (`products.xsd`) gestartet.
2. Das Programm validiert die Struktur und den Inhalt des XML-Dokuments.
3. Sind die Daten gültig, werden sie in eine Python-Datenstruktur geladen.
4. Die Daten werden dann in einer JSON-Datei (`products.json`) gespeichert.

### JSON Output (Beispiel):
```json
[
    {
        "id": "1",
        "name": "Product A",
        "price": 19.90,
        "category": "Electronics",
        "stock": 100
    },
    {
        "id": "2",
        "name": "Product B",
        "price": 5.50,
        "category": "Stationery",
        "stock": 200
    }
]
```