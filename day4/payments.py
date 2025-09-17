class payment:
    def pay(self,amount):
        print("")

class cashpayment:
    def pay(self,amount):
        print(f"paid {amount} in cash ")
        

class cardpayment:
    def pay(self,amount):
        print(f"paid {amount} using credit/debit card ")


class upipayment:
    def pay(self,amount):
        print(f"paid {amount} through upi ")

l1=[cashpayment(),cardpayment(),upipayment()]

for i in l1:
    i.pay(1000)

        