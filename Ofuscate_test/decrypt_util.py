from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_file(path, key, iv):
    with open(path, 'rb') as f:
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext
