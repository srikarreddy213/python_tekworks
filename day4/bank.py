class BankAcc:
    def __init__(self):
        self.__balance = 0  

    def deop(self, amount):
        self.__balance += amount  

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_bal(self):
        print(f"Balance: ₹{self.__balance}")



s = BankAcc()
s.deop(5000)
s.withdraw(112000)
s.get_bal()
