import cryptography
from cryptography.fernet import Fernet


def create_key():

    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    return open("key.key", "rb").read()

create_key()


key = load_key()

text = input('Message you want to encrypt: ')

message = text.encode()

f = Fernet(key)

encrypted = f.encrypt(message)
print(encrypted)







