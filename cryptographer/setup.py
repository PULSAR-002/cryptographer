from setuptools import setup, find_packages

setup(
    name="cryptographer",
    version="0.1",
    description="Terminal-based encryption and decryption tool by PULSAR",
    author="PULSAR",
    packages=find_packages(),
    install_requires=["cryptography", "rich"],
    entry_points={
        "console_scripts": [
            "cryptographer=cryptographer.core:main"
        ]
    }
)
