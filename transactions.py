import json

class Transaction:
    def __init__(self, sender, recipient, amount, signature):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount
        }

    def verify_signature(self, public_key):
        from ecdsa import VerifyingKey, SECP256k1, BadSignatureError
        try:
            vk = VerifyingKey.from_string(bytes.fromhex(public_key), curve=SECP256k1)
            vk.verify(bytes.fromhex(self.signature), json.dumps(self.to_dict()).encode())
            return True
        except BadSignatureError:
            return False
