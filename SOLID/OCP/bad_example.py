class PaymentProcessor:
    def pay(self, payment_method: str, amount:str):

        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print("UPI transaction finished")
        
        elif payment_method == "creadit_card":
            print(f"Starting creadit card transaction of Rs.{amount}")
            print("Creadit card transaction finished")
        
        elif payment_method == "net_banking":
            print(f"Starting net_banking transaction of Rs.{amount}")
            print("net_banking transaction finished")

pay_p = PaymentProcessor()
pay_p.pay("creadit_card",500)