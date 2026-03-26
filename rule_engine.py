class RuleEngine:

    ALLOWED_TRANSFERS = {
        "Pharma": ["Distributor"],
        "Distributor": ["Retailer"]
    }

    @staticmethod
    def is_allowed(sender, receiver):
        return receiver in RuleEngine.ALLOWED_TRANSFERS.get(sender, [])
