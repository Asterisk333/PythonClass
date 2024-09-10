# Sie haben eine Funktion namens "calculate_total_price" in Ihrem Python-Code, die den Gesamtpreis einer Bestellung
# basierend auf den Preisen und Mengen der einzelnen Produkte berechnet. Die Funktion verwendet eine externe
# Preistabelle, um die aktuellen Preise abzurufen. Schreiben Sie einen Unit-Test für diese Funktion, der mithilfe von
# Mocking sicherstellt, dass die Funktion die Preistabelle korrekt abruft und den Gesamtpreis richtig berechnet.
# Mocken Sie die Preistabelle, um den tatsächlichen externen Datenabruf zu vermeiden.

import unittest
from unittest.mock import patch

# Angenommen, calculate_total_price ist in einem Modul namens order_module
from order_module import calculate_total_price


class TestCalculateTotalPrice(unittest.TestCase):
    @patch('order_module.get_price_table')
    def test_calculate_total_price(self, mock_get_price_table):
        # Mock die Preistabelle
        mock_get_price_table.return_value = {'apple': 1.0, 'banana': 0.5}

        # Rufe die Funktion auf
        order = {'apple': 3, 'banana': 2}
        total_price = calculate_total_price(order)

        # Überprüfe, ob der Gesamtpreis korrekt berechnet wurde
        self.assertEqual(total_price, 4.0)


if __name__ == '__main__':
    unittest.main()
