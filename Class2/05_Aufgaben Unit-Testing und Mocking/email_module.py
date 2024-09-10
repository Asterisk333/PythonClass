import smtplib
from email.mime.text import MIMEText


class EmailSender:
    def send_email(self, to_address, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'your_email@example.com'
        msg['To'] = to_address

        with smtplib.SMTP('smtp.example.com') as server:
            server.login('your_username', 'your_password')
            server.send_message(msg)
