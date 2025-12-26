class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(5000)
acc.deposit(2000)
print("Balance:", acc.get_balance())
