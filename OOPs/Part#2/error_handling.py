#Custom exception class
class InsufficientFundsError(Exception):
    def __init__(self,balance,amount):
        super().__init__(f"Insufficient Amount: Your current balance is {balance} and your requested amount is {amount}.")
        self.balance = balance
        self.amount = balance

class BankAccount:
    def __init__(self,name):
        self.name = name
        self.balance = 2000

    def balance_withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < amount:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

try:
    withdraw = BankAccount("Ali")
    withdraw.balance_withdraw(1000)
except Exception as e:
    print(e)
    
