class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
#child class

class SavingsAccount(BankAccount):
    def __init__(self,owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    def account_type(self):
        print("Savings Account")

#second child
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # child-specific behavior
        print("Processing current account withdrawal...")
        # use parent's withdrawal logic
        super().withdraw(amount)
    def account_type(self):
        print("Current Account")

accounts = [
    SavingsAccount("Upendra", 1000, 5),
    CurrentAccount("Upendra", 2000)
]
for account in accounts:
    account.account_type()


current = CurrentAccount("Upendra", 1000)

print( current.balance)

current.withdraw(300)

print("Balance:", current.balance)

current.withdraw(1000)

print("Balance:", current.balance)
