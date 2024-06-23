from cryptography.fernet import Fernet
import GenerateKey

key_manager = GenerateKey.KeyManager()
encryption_key = key_manager.GetKey()
cipher = Fernet(encryption_key)

log_file = "encrypted_log.txt"

def read_encrypted_log():
    with open(log_file, "rb") as f:
        for line in f:
            encrypted_data = line.strip()
            decrypted_data = cipher.decrypt(encrypted_data).decode()
            print(decrypted_data, end="")

read_encrypted_log()
