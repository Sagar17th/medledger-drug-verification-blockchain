from blockchain import Blockchain
from secure_transfer import SecureTransfer
from rule_engine import RuleEngine
from database import Database
import json

blockchain = Blockchain()
db = Database()

def create_transaction():
    sender = input("Enter sender (Pharma / Distributor): ").strip()
    receiver = input("Enter receiver (Distributor / Retailer): ").strip()
    data = input("Enter product / batch details: ").strip()

    if not RuleEngine.is_allowed(sender, receiver):
        print("❌ Transfer not allowed by business rules")
        return

    signature = SecureTransfer.sign_data(
        data, f"keys/{sender}_private.pem"
    )

    verified = SecureTransfer.verify_data(
        data, signature, f"keys/{sender}_public.pem"
    )

    if not verified:
        print("❌ Signature verification failed")
        return

    transaction = {
        "from": sender,
        "to": receiver,
        "data": data,
        "signature": signature
    }

    db.save_transaction(transaction)
    blockchain.add_block(transaction)

    print("✅ Transaction successfully added to blockchain")


def view_transactions():
    transactions = db.get_all_transactions()
    if not transactions:
        print("⚠️ No transactions found")
        return

    print("\n📄 Transactions:")
    for i, tx in enumerate(transactions, start=1):
        print(f"\nTransaction {i}:")
        print(json.dumps(tx, indent=4))


def view_blockchain():
    print("\n🔗 Blockchain:")
    for block in blockchain.chain:
        print(f"\nBlock #{block.index}")
        print(f"Timestamp     : {block.timestamp}")
        print(f"Previous Hash : {block.previous_hash}")
        print(f"Hash          : {block.hash}")
        print(f"Data          : {block.data}")


def verify_blockchain():
    if blockchain.is_valid():
        print("✅ Blockchain integrity verified (No tampering)")
    else:
        print("❌ Blockchain compromised!")


def menu():
    while True:
        print("\n==============================")
        print(" MEDLEDGER BLOCKCHAIN SYSTEM ")
        print("==============================")
        print("1. Create new transaction")
        print("2. View all transactions")
        print("3. View blockchain")
        print("4. Verify blockchain integrity")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            create_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_blockchain()
        elif choice == "4":
            verify_blockchain()
        elif choice == "5":
            print("👋 Exiting system")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
