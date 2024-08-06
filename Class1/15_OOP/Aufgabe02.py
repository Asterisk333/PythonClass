# Eine Restaurantklasse definieren
class Restaurant:
    # Ein Konstruktor mit drei Instanzattributen: menu_items, book_table und customer_orders
    def __init__(self):
        self.menu_items = {}  # Ein leeres Wörterbuch für die Menüpunkte
        self.book_table = []  # Eine leere Liste für die Tischreservierungen
        self.customer_orders = []  # Eine leere Liste für die Kundenbestellungen

    # Eine Methode, um einen Menüpunkt hinzuzufügen
    def add_item_to_menu(self, name, price):
        self.menu_items[name] = price  # Den Namen und den Preis des Menüpunkts dem Wörterbuch hinzufügen

    # Eine Methode, um einen Tisch zu reservieren
    def book_table(self, number, time):
        self.book_table.append(time)  # Die Tischnummer und die Zeit der Reservierung der Liste hinzufügen

    # Eine Methode, um eine Kundenbestellung aufzunehmen
    def customer_order(self, table, items):
        self.customer_orders.append(
            (table, items))  # Die Tischnummer und die bestellten Menüpunkte der Liste hinzufügen

    # Eine Methode, um die Speisekarte auszudrucken
    def print_menu(self):
        print("Speisekarte:")
        for name, price in self.menu_items.items():  # Durch das Wörterbuch der Menüpunkte iterieren
            print(f"- {name}: {price} CHF")  # Den Namen und den Preis jedes Menüpunkts ausgeben

    # Eine Methode, um die Tischreservierungen auszudrucken
    def print_book_table(self):
        print("Tischreservierungen:")
        for number, time in self.book_table:  # Durch die Liste der Tischreservierungen iterieren
            print(f"- Tisch {number}: {time}")  # Die Tischnummer und die Zeit jeder Reservierung ausgeben

    # Eine Methode, um die Kundenbestellungen auszudrucken
    def print_customer_orders(self):
        print("Kundenbestellungen:")
        for table, items in self.customer_orders:  # Durch die Liste der Kundenbestellungen iterieren
            print(
                f"- Tisch {table}: {', '.join(items)}")  # Die Tischnummer und die bestellten Menüpunkte jeder Bestellung ausgeben


# Ein Objekt der Restaurantklasse erstellen
restaurant = Restaurant()

# Einige Menüpunkte hinzufügen
restaurant.add_item_to_menu("Pizza Margherita", 15)
restaurant.add_item_to_menu("Spaghetti Bolognese", 12)
restaurant.add_item_to_menu("Salat", 8)
restaurant.add_item_to_menu("Eis", 5)

# Einige Tischreservierungen vornehmen
restaurant.book_table("18:00")
restaurant.book_table("19:00")
restaurant.book_table("20:00")

# Einige Kundenbestellungen aufnehmen
restaurant.customer_order(1, ["Pizza Margherita", "Salat"])
restaurant.customer_order(2, ["Spaghetti Bolognese", "Eis"])
restaurant.customer_order(3, ["Salat", "Eis"])

# Die Speisekarte ausdrucken
restaurant.print_menu()

# Die Tischreservierungen ausdrucken
restaurant.print_book_table()

# Die Kundenbestellungen ausdrucken
restaurant.print_customer_orders()
