class CryptoWallet:
    def __init__(self, owner):
        """Initialize a new CryptoWallet instance with owner's name, balances, and an empty transaction history."""
        self.owner = owner
        self.balances = {}
        self.transactions = []

    def deposit(self, currency, amount):
        """Deposit a specified amount of a cryptocurrency and record the transaction."""
        if amount > 0:
            if currency in self.balances:
                self.balances[currency] += amount
            else:
                self.balances[currency] = amount
            print(f"Deposited {amount} {currency}.")
            self.transactions.append((currency, amount, 'deposit'))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, currency, amount):
        """Withdraw a specified amount of a cryptocurrency and record the transaction."""
        if amount > 0 and currency in self.balances and self.balances[currency] >= amount:
            self.balances[currency] -= amount
            print(f"Withdrew {amount} {currency}.")
            self.transactions.append((currency, -amount, 'withdrawal'))
        else:
            print("Insufficient funds or currency not found.")

    def check_balance(self, currency):
        """Return the current balance of a specific cryptocurrency."""
        return self.balances.get(currency, 0)

    def get_transaction_history(self):
        """Return the transaction history."""
        return self.transactions

# Example usage:
wallet = CryptoWallet("Alex")
wallet.deposit("Bitcoin", 0.1)
wallet.deposit("Ethereum", 2)
print("Bitcoin balance:", wallet.check_balance("Bitcoin"))
print("Ethereum balance:", wallet.check_balance("Ethereum"))
wallet.withdraw("Bitcoin", 0.05)
print("Bitcoin balance after withdrawal:", wallet.check_balance("Bitcoin"))