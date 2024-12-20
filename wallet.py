import os
import json
from ecdsa import SigningKey, SECP256k1
import hashlib

class Wallet:
    def __init__(self, wallet_file='wallet.json'):
        self.wallet_file = wallet_file
        if os.path.exists(self.wallet_file):
            self.load_wallet()
        else:
            self.create_wallet()

    def create_wallet(self):
        self.private_key = SigningKey.generate(curve=SECP256k1)
        self.public_key = self.private_key.get_verifying_key()
        self.address = self.generate_address()
        self.save_wallet()
        print(f"New wallet created. Address: {self.address}")

    def load_wallet(self):
        with open(self.wallet_file, 'r') as f:
            data = json.load(f)
            self.private_key = SigningKey.from_string(bytes.fromhex(data['private_key']), curve=SECP256k1)
            self.public_key = self.private_key.get_verifying_key()
            self.address = data['address']
            print(f"Wallet loaded. Address: {self.address}")

    def save_wallet(self):
        data = {
            'private_key': self.private_key.to_string().hex(),
            'public_key': self.public_key.to_string().hex(),
            'address': self.address
        }
        with open(self.wallet_file, 'w') as f:
            json.dump(data, f)   #test

    def generate_address(self):
        public_key_bytes = self.public_key.to_string()
        sha256 = hashlib.sha256(public_key_bytes).hexdigest()
        ripemd160 = hashlib.new('ripemd160', bytes.fromhex(sha256)).hexdigest()
        return ripemd160

    def sign_transaction(self, transaction):
        return self.private_key.sign(transaction.encode()).hex()

    def get_public_key(self):
        return self.public_key.to_string().hex()
