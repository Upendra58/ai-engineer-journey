class Payment:
    def __init__(self, customer,amount):
        self.customer = customer
        self.__amount = amount
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self,value):
        if value > 0:
            self.__amount = value
        else:
            print("Amount must be greater than 0")
    def show_payment(self):
        print(f"Customer: {self.customer}")
        print(f"amount: {self.__amount}")
    def process_payment(self):
        print("Payment processing")
class CreditCardPayment(Payment):
    def __init__(self, customer, amount):
        super().__init__(customer,amount)
    def process_payment(self):
        print("Processing Credit Card payment")
class UPIPayment(Payment):
    def __init__(self,customer,amount):
        super().__init__(customer,amount)
    def process_payment(self):
        print("Processing UPI payment")
payments = [
    CreditCardPayment("Upendra", 1500),
    UPIPayment("Rahul", 800),
    Payment("John", 500)
]
for payment in payments:
    payment.process_payment()