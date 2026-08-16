from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, balance:int):
        self.balance = balance
        
    @abstractmethod
    def deposit(self,amount):
        pass
    
    @abstractmethod
    def withdraw(self, amount):
        pass

class SavingAccount(BankAccount):
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

class FD(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)
    
    def withdraw(self,amount):
        
        raise Exception("Cannot withdraw from FD")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Total balance : {self.balance}")

# saving = SavingAccount(1000)
# saving.deposit(100)
# saving.withdraw(300)

fd = FD(4000)
fd.deposit(100)
fd.withdraw(300)