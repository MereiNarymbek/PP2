class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"

    def Deposit(self, money):
        self.balance += money
        print(f"Deposited: {money} and New balance: {self.balance} ")
        
    def Withdraw(self, cash):
        if cash > self.balance:
            print("Impossible to withdraw")
        else :
            self.balance -= cash
            print(f"Withdrew: {cash} and New balance: {self.balance}")
            
account = Account("Nurzhau", 3500)
print(account)
account.Deposit(700) 
account.Withdraw(4000) 
account.Withdraw(250) 