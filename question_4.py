class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

Account("Ashish", 5000)        
Account("Ashish", 5000, 5)

