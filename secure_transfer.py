from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class SecureTransfer:

    @staticmethod
    def sign_data(data, private_key_path):
        private_key = RSA.import_key(open(private_key_path).read())
        hash_data = SHA256.new(data.encode())
        signature = pkcs1_15.new(private_key).sign(hash_data)
        return signature.hex()

    @staticmethod
    def verify_data(data, signature, public_key_path):
        public_key = RSA.import_key(open(public_key_path).read())
        hash_data = SHA256.new(data.encode())

        try:
            pkcs1_15.new(public_key).verify(
                hash_data,
                bytes.fromhex(signature)
            )
            return True
        except:
            return False
