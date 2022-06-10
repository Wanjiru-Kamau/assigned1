class Account:
    def __init__(self, account_name, account_number):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = 0
        self.deposits=[]
        self.withdraws=[]

    def deposit(self,amount):
        if amount<=0:
            return f"Deposit must be positive"

        else:
            self.balance += amount
            self.deposits.append(amount)
        return f"Hello {self.account_name} you made a deposit of {amount} and your balance is {self.balance}."

    def withdraw(self, withdrawal):
        self.transaction=100
        if withdrawal<=self.balance and withdrawal>0:
         self.balance -= withdrawal+self.transaction
         self.withdraws.append(withdrawal)
        else:
             return f"You cant withdraw"
        return f"Hello {self.account_name}, you made a withdrawal of {withdrawal} your new balance is {self.balance}."
    def  deposits_statement(self):
        for x in self.deposits:
            print(x,end="\n") 

    def  withdraws_statement(self):
        for x in self.withdraws:
            print(x,end="\n") 
    def current_balance(self):
        return f"{self.balance}"                 