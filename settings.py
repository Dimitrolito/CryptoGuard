# Install Required Libraries
# pip install bitcoinlib flask

# Generate Private and Public Keys
from bitcoinlib.keys import Key

# Generate a new key
key = Key()

# Private key
private_key = key.wif
print(f"Private Key (WIF): {private_key}")

# Public key
public_key = key.public_hex
print(f"Public Key: {public_key}")

# Wallet address
address = key.address
print(f"Wallet Address: {address}")
