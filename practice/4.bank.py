#bank with account,deposit,withdrawal,andh checking balance

class Bank:
    def __init__(self):
        self.total_amount = 0

    def deposit(self,money):
        self.total_amount  = self.total_amount + money
        print(f'{money} money deposited')

    def withdraw(self,money):
        self.total_amount = self.total_amount - money
        print(f'{money} money withdrawn')
    def check_balance(self):
        print(f'balnce is {self.total_amount}')

b = Bank()
b.deposit(1000)
b.withdraw(500)
b.check_balance()