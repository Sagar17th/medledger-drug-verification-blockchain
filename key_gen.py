from blockchain import Blockchain
from secure_transfer import SecureTransfer
from rule_engine import RuleEngine
from database import Database

def main():
    print("🚀 Starting Secure Blockchain Transaction")

    blockchain = Blockchain()
    db = Database()

    sender = "Pharma"
    receiver = "Distributor"
    data = "Medicine Batch #A123"

    print(f"Sender     : {sender}")
    print(f"Receiver   : {receiver}")
    print(f"Data       : {data}")

    # Rule check
    if not RuleEngine.is_allowed(sender, receiver):
        print("❌ Transfer not allowed by rules")
        return

    print("✅ Transfer allowed")

    # Sign data
    signature = SecureTransfer.sign_data(
        data, f"keys/{sender}_private.pem"
    )
    print("✍ Data signed")

    # Verify signature
    verified = SecureTransfer.verify_data(
        data, signature, f"keys/{sender}_public.pem"
    )

    if not verified:
        print("❌ Signature verification failed")
        return

    print("🔐 Signature verified")

    transaction = {
        "from": sender,
        "to": receiver,
        "data": data,
        "signature": signature
    }

    db.save_transaction(transaction)
    blockchain.add_block(transaction)

    print("📦 Transaction added to blockchain")
    print("🔗 Blockchain valid:", blockchain.is_valid())


if __name__ == "__main__":
    main()
