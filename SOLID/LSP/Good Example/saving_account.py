from withdrawable_account import Withdrawable

class SavingAccount(Withdrawable):
    def __init__(self, balance):
        super().__init__(balance)
        
    def withdraw(self,amount):   
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn {amount}, remaining balance {self.balance}")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Total balance : {self.balance}")