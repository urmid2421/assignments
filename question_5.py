class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def getBalance(self):
        print(self.balance)

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
            super().__init__(title, balance)
            self.interestRate = interestRate

    def interestAmount(self):
            print(self.interestRate*self.balance / 100)

obj = Account("Ashish", 2000)
obj.deposit(500)
obj.getBalance()

obj = Account("Ashish", 2000)
obj.withdrawal(500)
obj.getBalance()

sa = SavingsAccount("Ashish", 2000,5)
sa.interestAmount()