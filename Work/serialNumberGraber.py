import subprocess
import getpass


def get_remote_serial_number(computer_name, username, password):
    # Befehl für Windows Remote Management
    command = f"wmic /node:{computer_name} /user:{username} /password:{password} bios get serialnumber"
    try:
        serial_number = subprocess.check_output(command, shell=True).decode().split('\n')[1].strip()
        return serial_number
    except subprocess.CalledProcessError as e:
        return f"Fehler beim Auslesen der Seriennummer: {e}"


# Benutzernamen und Passwort unleserlich einlesen
computer = input("Geben Sie den Computernamen ein: ")
user = input("Geben Sie den Benutzernamen ein: ")
print("user is durch")
pwd = getpass.getpass()

# Seriennummer ausgeben
print(f"Seriennummer: {get_remote_serial_number(computer, user, pwd)}")
