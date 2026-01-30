class BankAccount:
    def __init__(self, balance):
        self.balace = balance

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balace - other.balace
            new_account = BankAccount(new_balance)
            return new_account
        return None


    def __add__(self, other):
        if not isinstance(other, BankAccount):
            new_balance = self.balace + other.balace
            new_account = BankAccount(new_balance)
            return new_account
        return None


    def __str__(self):
        return f"BankAccount: {self.balace:,.2f}"