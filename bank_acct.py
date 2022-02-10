class BankAccount:

    def __init__(self, int_rate, balance, name):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self
        

    def display_account_info(self):
        print(f"Account owner: {self.name}, has a Balance of: {self.balance}, with a APR of: {self.int_rate}%")
        return self

    def yield_interest(self):
        self.balance += self.int_rate * self.balance
        return self

#owners
danniel = BankAccount(.02, 0, "Danniel")
sara = BankAccount(.01, 0, "Sara")

#actions
danniel.deposit(100).deposit(100).deposit(300).withdraw(50).yield_interest().display_account_info()
sara.deposit(1000).deposit(1000).withdraw(500).withdraw(100).withdraw(125).withdraw(50).yield_interest().display_account_info()