import os
from cryptography.fernet import Fernet
from rich import print
from . import banner

def generate_key(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"[bold green]✅ Key generated and saved at:[/bold green] {key_path}")

def load_key(key_path):
    if not os.path.exists(key_path):
        raise FileNotFoundError(f"Key not found at {key_path}")
    with open(key_path, "rb") as key_file:
        return key_file.read()

def encrypt_file(file_path, key_path):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted_data = cipher.encrypt(data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    print(f"[bold green]🔐 Data encrypted successfully![/bold green]")
    print(f"[cyan]🗝️ Key saved at: {key_path}[/cyan]")

def decrypt_file(file_path, key_path):
    key = load_key(key_path)
    cipher = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = cipher.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    print(f"[bold green]✅ Data decrypted successfully![/bold green]")

import argparse

def main():
    banner()
    parser = argparse.ArgumentParser(
        description="🔐 Cryptographer - Encrypt or Decrypt any file using Fernet"
    )
    subparsers = parser.add_subparsers(dest="command", help="encrypt or decrypt")

    # Encrypt command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    encrypt_parser.add_argument("--data", required=True, help="Path to the file to encrypt")
    encrypt_parser.add_argument("--key", required=True, help="Path to save the encryption key")

    # Decrypt command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    decrypt_parser.add_argument("--data", required=True, help="Path to the file to decrypt")
    decrypt_parser.add_argument("--key", required=True, help="Path to the key file")

    args = parser.parse_args()

    if args.command == "encrypt":
        encrypt_file(args.data, args.key)
    elif args.command == "decrypt":
        decrypt_file(args.data, args.key)
    else:
        parser.print_help()
