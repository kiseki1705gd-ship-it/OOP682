from models.BK import BankAccount

my_account = BankAccount(1000)
your_account = BankAccount(1500)

our_account = my_account + your_account
our_account = my_account - your_account
print(our_account)