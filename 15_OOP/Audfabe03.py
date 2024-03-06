# Eine Inventoryklasse definieren
class Inventory:
    # Ein Konstruktor mit einem Instanzattribut: items
    def __init__(self):
        self.items = {}  # Ein leeres Wörterbuch für die Artikeldetails

    # Eine Methode, um einen Artikel hinzuzufügen
    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {"item_name": item_name,
                               "stock_count": stock_count,
                               "price": price}  # Den Artikel mit seiner ID und einem Wörterbuch seiner Details dem Wörterbuch hinzufügen

    # Eine Methode, um einen Artikel zu aktualisieren
    def update_item(self, item_id, item_name=None, stock_count=None, price=None):
        if item_id in self.items:  # Überprüfen, ob der Artikel mit der gegebenen ID existiert
            if item_name is not None:  # Wenn ein neuer Name gegeben ist, diesen aktualisieren
                self.items[item_id]["item_name"] = item_name
            if stock_count is not None:  # Wenn eine neue Anzahl gegeben ist, diese aktualisieren
                self.items[item_id]["stock_count"] = stock_count
            if price is not None:  # Wenn ein neuer Preis gegeben ist, diesen aktualisieren
                self.items[item_id]["price"] = price
        else:  # Wenn der Artikel mit der gegebenen ID nicht existiert, eine Fehlermeldung ausgeben
            print(f"Artikel mit ID {item_id} nicht gefunden.")

    # Eine Methode, um die Artikeldetails zu überprüfen
    def check_item_details(self, item_id):
        if item_id in self.items:  # Überprüfen, ob der Artikel mit der gegebenen ID existiert
            return self.items[item_id]  # Das Wörterbuch mit den Artikeldetails zurückgeben
        else:  # Wenn der Artikel mit der gegebenen ID nicht existiert, eine Fehlermeldung ausgeben
            print(f"Artikel mit ID {item_id} nicht gefunden.")


reee = Inventory()

reee.add_item(1, "Paltop", 4, 3)

reee.add_item(2, "sdfndgsdg", 4, 3)

reee.check_item_details(1)
