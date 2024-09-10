def get_price_table():
    # Diese Funktion würde normalerweise die Preistabelle von einer externen Quelle abrufen
    return {'apple': 1.0, 'banana': 0.5}


def calculate_total_price(order):
    price_table = get_price_table()
    total_price = sum(price_table[item] * quantity for item, quantity in order.items())
    return total_price
