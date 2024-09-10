# Sie haben eine Funktion namens "get_user_data" in Ihrem Python-Code, die eine HTTP-Anfrage an eine externe API
# sendet und die Benutzerdaten abruft. Schreiben Sie einen Unit-Test für diese Funktion, der mithilfe von Mocking das
# Verhalten der externen API simuliert und überprüft, ob die Funktion die erwarteten Benutzerdaten zurückgibt.

import unittest
from unittest.mock import patch
import requests

# Angenommen, get_user_data ist in einem Modul namens my_module
from user_data_module import get_user_data


class TestGetUserData(unittest.TestCase):
    @patch('my_module.requests.get')
    def test_get_user_data(self, mock_get):
        # Mock die Antwort der API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'John Doe'}

        # Rufe die Funktion auf
        result = get_user_data()

        # Überprüfe, ob die Funktion die erwarteten Daten zurückgibt
        self.assertEqual(result, {'id': 1, 'name': 'John Doe'})


if __name__ == '__main__':
    unittest.main()
