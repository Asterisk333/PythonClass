import io

from updater import check_for_update

# Prüft auf Updates, bevor das eigentliche Programm startet
#check_for_update()

#main Code
from dotenv import dotenv_values
import json
from decrypt_util import decrypt_file


key = b'ne_super_geheime_key123456789012'
iv = b'starter_vector_1'

# .env entschlüsseln
env_bytes = decrypt_file("assets/.env.enc", key, iv)

# Dekodiere die Bytes in einen String
env_string = env_bytes.decode()

# Verwende StringIO, um den String in einen Stream umzuwandeln
import io
env_stream = io.StringIO(env_string)

# Lade die Umgebungsvariablen
env = dotenv_values(stream=env_stream)

# Setze die geladenen Variablen als globale Variablen
globals().update(env)

# client_secrets.json entschlüsseln
secrets_bytes = decrypt_file("assets/client_secrets.json.enc", key, iv)
secrets = json.loads(secrets_bytes.decode())

print("ENV VARIABLEN:")
print(KEY)
print("GOOGLE CLIENT SECRETS:")
print(secrets)