class CryptoWallet:
    SUPPORTED_CURRENCIES = {'Bitcoin', 'Ethereum', 'Ripple', 'Litecoin'}

    def __init__(self, owner):
        """Initialize a new CryptoWallet instance."""
        self.owner = owner
        self.balances = {}
        self.transactions = []

    def deposit(self, currency, amount):
        """Deposit a specified amount of a supported cryptocurrency."""
        if currency not in self.SUPPORTED_CURRENCIES:
            print(f"Currency {currency} is not supported.")
            return
        if amount > 0:
            self.balances[currency] = self.balances.get(currency, 0) + amount
            print(f"Deposited {amount} {currency}.")
            self.transactions.append((currency, amount, 'deposit'))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, currency, amount):
        """Withdraw a specified amount from the wallet if the currency is supported and funds are available."""
        if currency not in self.SUPPORTED_CURRENCIES:
            print(f"Currency {currency} is not supported.")
            return
        if amount > 0 and self.balances.get(currency, 0) >= amount:
            self.balances[currency] -= amount
            print(f"Withdrew {amount} {currency}.")
            self.transactions.append((currency, -amount, 'withdrawal'))
        else:
            print("Insufficient funds or currency not found.")

    def check_balance(self, currency):
        """Check the balance of a specific cryptocurrency, ensuring it's supported."""
        if currency not in self.SUPPORTED_CURRENCIES:
            print(f"Currency {currency} is not supported.")
            return 0
        return self.balances.get(currency, 0)

# Example usage:
wallet = CryptoWallet("Alex")
wallet.deposit("Bitcoin", 0.1)
wallet.deposit("Ethereum", 2)
print("Bitcoin balance:", wallet.check_balance("Bitcoin"))
print("Ethereum balance:", wallet.check_balance("Ethereum"))
wallet.withdraw("Bitcoin", 0.05)
print("Bitcoin balance after withdrawal:", wallet.check_balance("Bitcoin"))