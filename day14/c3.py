class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("No sufficient balance")
    def display_balance(self):
        print(f" Total balance: {self.balance}")

acc1 = BankAccount("Upendra", 45000)
acc1.display_balance()
acc1.deposit(5000)
acc1.display_balance()
acc1.withdraw(34000)
acc1.display_balance()
acc1.withdraw(350000)
acc1.display_balance()