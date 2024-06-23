from cryptography.fernet import Fernet
import os

class KeyManager:
    def __init__(self, File="Key.key"):
        self.KeyFile = File

    def GetKey(self):
        if os.path.exists(self.KeyFile):
            with open(self.KeyFile, "rb") as key_file:
                key = key_file.read()
        else:
            key = Fernet.generate_key()
            with open(self.KeyFile, "wb") as key_file:
                key_file.write(key)
        return key

# Example usage
# key_manager = KeyManager()
# encryption_key = key_manager.GetKey()
# print(encryption_key)
