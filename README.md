# 🔐 Cryptographer by PULSAR

**Cryptographer** is a simple, terminal-based encryption and decryption tool built with Python and powered by the [cryptography](https://cryptography.io/en/latest/) library.  
It uses **Fernet symmetric encryption**, allowing you to securely encrypt any file using an auto-generated key — perfect for securing notes, passwords, and sensitive documents.

---

## ✨ Features

- 🔒 File-based encryption using Fernet (symmetric encryption)
- 🗝️ Automatic key generation and saving to user-defined path
- 🔓 Secure decryption using saved key
- 🖥️ Terminal-based CLI interface — easy to use
- 🐍 100% Python

---

## 🛠️ Installation

### 🔗 Clone the repository
<pre>
git clone https://github.com/PULSAR-002/cryptographer.git
cd cryptographer
cd cryptographer (list the items to see the setup.py file, if it is present then enter the following command)
pip install .
</pre>
## Install the requirements in virtual environment(recommended)
<pre>
  pip install -r requirements.txt
</pre>

## USAGE:
## Encryption:
<pre>
  cryptographer encrypt --data /path/of/data/to_encrypt.txt --key /path/to/save/the_key.key
</pre>
## Decryption:
<pre>
  cryptographer decrypt --data path/to/encrypted_file.txt --key path/to/your/key.key
</pre>
## Use the same to key to decrypt that you used to encrypt
