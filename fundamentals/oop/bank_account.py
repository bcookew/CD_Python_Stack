class BankAccount:
    accts = []
    def __init__(self, openingBal=0, interestRate=0.01):
        self.balance = openingBal
        self.interestRate = interestRate
        BankAccount.accts.append(self)
        print(f"New Account Opened.\nOpening Bal: ${self.balance}\nInterest Rate: {self.interestRate}%\n")

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if(BankAccount.sufficientFunds(self.balance, amount)):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def displayAccountInfo(self):
        print(f"Balance: {self.balance}")
        return self

    def yieldInterest(self):
        if(BankAccount.sufficientFunds(self.balance, 0)):
            self.balance = self.balance + (self.balance * self.interestRate)
        return self

    @classmethod
    def listAccounts(cls):
        for acct in BankAccount.accts:
            acct.displayAccountInfo()

    @staticmethod
    def sufficientFunds(bal,amount):
        if bal - amount >= 0:
            return True
        else:
            return False


acct1 = BankAccount()
acct2 = BankAccount(100, 0.05)

acct1.deposit(100).deposit(400).withdrawal(450).displayAccountInfo()
acct2.deposit(500).deposit(500).withdrawal(25).withdrawal(25).withdrawal(25).withdrawal(25).yieldInterest().displayAccountInfo()
BankAccount.listAccounts()
