from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = b'ne_super_geheime_key123456789012'  # 32 bytes!
iv = b'starter_vector_1'  # 16 bytes!

def encrypt_file(path):
    with open(path, 'rb') as f:
        plaintext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(path + '.enc', 'wb') as f:
        f.write(ciphertext)

encrypt_file('assets/.env')
encrypt_file('assets/client_secrets.json')
