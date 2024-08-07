class BankAccount:
    def __init__(self, initial_balance, account_name):
        self.balance = initial_balance
        self.name=account_name
        print(f"Bank Account {self.name} created \n Balance:$ {self.balance}")

    def get_balance(self):
        print(f"\nBank Account {self.name} balance is: $ {self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\n Deposit succesful {self.name}, the new amount is: $ {self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than the balance")
        else:
            amount = self.balance-amount
            print(f"\n Withdraw succesful {self.name}, the new amount is: $ {amount:.2f}")

    def transfer(self, account_namee, amount):
        if amount > self.balance:
            raise ValueError("Amount cannot be greater than the balance")
        else:
            account_namee.deposit(amount)

class interestRewards(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.1)
        self.get_balance()

class savingsaccount(interestRewards):
    def __init__(self, initial_balance, account_name):
        super().__init__(initial_balance, account_name)
        self.fee = 10

    def withdraw(self, amount):
        if amount > self.balance+self.fee:
            raise ValueError("Amount cannot be greater than the balance and fee of 10")
        else:
            self.balance=self.balance-(amount+self.fee)
            print(f"\n Withdraw succesful , the new amount is: $ {self.balance:.2f}")









