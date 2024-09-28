from bitcoinlib.keys import Key, Address
from bitcoinlib.services.services import Service
from bitcoinlib.transactions import Transaction
from cryptography.fernet import Fernet

# Generate keys
key = Key()
private_key = key.wif
public_key = key.public_hex
address = key.address

print(f"Private Key (WIF): {private_key}")
print(f"Public Key: {public_key}")
print(f"Wallet Address: {address}")

# Initialize service
service = Service()

# Get balance
balance = service.getbalance(address.address)
print(f"Balance: {balance} BTC")

# Generate encryption key
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Encrypt the private key
encrypted_private_key = cipher_suite.encrypt(private_key.encode())
with open('private_key.enc', 'wb') as f:
    f.write(encrypted_private_key)
print("Private key encrypted and saved in 'private_key.enc'")

# Example of sending a transaction (replace with a valid address and amount)
# to_address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'
# amount = 0.001
# tx = Transaction()
# tx.add_input(address.address, amount)
# tx.add_output(to_address, amount)
# tx.sign(key)
# tx_id = service.sendrawtransaction(tx.raw_hex())
# print(f"Transaction sent. ID: {tx_id}")
