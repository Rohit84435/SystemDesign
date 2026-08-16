from account import Account
from abc import abstractmethod

class Withdrawable(Account):
    
    def __init__(self, balance):
        super().__init__(balance)
        
    @abstractmethod
    def withdraw(self, amount):
        pass