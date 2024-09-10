# Sie haben eine Klasse namens "EmailSender", die eine Methode "send_email" enthält, die eine E-Mail an eine
# angegebene Adresse sendet. Schreiben Sie einen Unit-Test für diese Methode, der mithilfe von Mocking überprüft,
# ob die Methode den erwarteten E-Mail-Text an die richtige Adresse sendet. Verwenden Sie ein Mock-Objekt,
# um den tatsächlichen E-Mail-Versand zu simulieren.

import unittest
from unittest.mock import patch, MagicMock

# Angenommen, EmailSender ist in einem Modul namens email_module
from email_module import EmailSender


class TestEmailSender(unittest.TestCase):
    @patch('email_module.smtplib.SMTP')
    def test_send_email(self, mock_smtp):
        # Erstelle eine Instanz von EmailSender
        email_sender = EmailSender()

        # Mock die SMTP-Instanz
        instance = mock_smtp.return_value

        # Rufe die Methode send_email auf
        email_sender.send_email('test@example.com', 'Test Subject', 'Test Body')

        # Überprüfe, ob die Methode send_message mit den richtigen Parametern aufgerufen wurde
        instance.send_message.assert_called_once()
        sent_message = instance.send_message.call_args[0][0]
        self.assertEqual(sent_message['To'], 'test@example.com')
        self.assertEqual(sent_message['Subject'], 'Test Subject')
        self.assertEqual(sent_message.get_payload(), 'Test Body')


if __name__ == '__main__':
    unittest.main()
