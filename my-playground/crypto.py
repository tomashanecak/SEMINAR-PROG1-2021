import os
from cryptography import fernet
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    crypto = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = crypto.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    crypto = Fernet(key)

    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()

    # decrypt data
    decrypted_data = crypto.decrypt(encrypted_data)

    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

#generate_key()
key = load_key()

file = "fotka.jpeg"
decrypt(file, key)

# crypto = Fernet(key)
# message = "Hello World".encode()
# encrypted_msg = crypto.encrypt(message)
# decrypted_msg = crypto.decrypt(encrypted_msg)
# print(encrypted_msg)
# print(decrypted_msg)