from cryptography.fernet import Fernet
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("🔐 Key generated and saved to 'secret.key'")
def load_key():
    return open("secret.key", "rb").read()
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as file:
        file.write(encrypted)
    print(f"🔒 File '{filename}' encrypted.")
def decrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(filename, "wb") as file:
        file.write(decrypted)
    print(f"🔓 File '{filename}' decrypted.")
if __name__ == "__main__":
    print("1. Generate Key\n2. Encrypt File\n3. Decrypt File")
    choice = input("Choose an option (1/2/3): ")
    if choice == "1":
        generate_key()
    elif choice == "2":
        file_name = input("Enter the file name to encrypt: ")
        encrypt_file(file_name)
    elif choice == "3":
        file_name = input("Enter the file name to decrypt: ")
        decrypt_file(file_name)
    else:
        print("Invalid choice!")