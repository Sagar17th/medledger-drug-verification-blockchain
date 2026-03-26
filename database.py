class Database:
    def __init__(self):
        self.transactions = []

    def save_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_all_transactions(self):
        return self.transactions
