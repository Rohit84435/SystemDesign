from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    
    @abstractmethod
    def pay(self,amount:int):
        pass
    
class UPIPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through upi amount {amount}")
        
class DebitCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through debitCard amount {amount}")

class CreditCardPayment(PaymentMethod):
    def pay(self,amount:int):
        print(f"Paying through CreaditCard amount {amount}")

class NetBankingPayment(PaymentMethod):
    def pay(self,amount):
        print(f"Paying through Net amount {amount}")

class PaymentProcessor:
    def process_payment(self, payment_method:PaymentMethod, amount:int):
        payment_method.pay(amount)

credit = CreditCardPayment()
debit = DebitCardPayment()
net = NetBankingPayment()

payment_process = PaymentProcessor()
payment_process.process_payment(net,500) 