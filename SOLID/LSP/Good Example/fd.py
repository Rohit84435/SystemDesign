from account import Account

class FD(Account):
    def __init__(self, balance):
        super().__init__(balance)
        
    def deposit(self,amount):
        self.balance += amount
        print(f"Your current FD balance :{self.balance}")