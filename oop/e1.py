class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0  and  amount <= self.__balance:
            self.__balance -= amount
        else:
            print("No sufficient Balance")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)
print(account.get_balance())

account.withdraw(300)
print("Balance:", account.get_balance())

account.withdraw(2000)
print("Balance:", account.get_balance())