import cryptography
from cryptography.fernet import Fernet





def load_key():
    return open("key.key", "rb").read()



key = load_key()

text = input('Message you want to decrypt: ')

message = text.encode()

f = Fernet(key)

decrypted_encrypted = f.decrypt(text)
print(decrypted_encrypted)



