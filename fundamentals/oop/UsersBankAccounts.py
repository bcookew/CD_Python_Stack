from secrets import choice


class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = [BankAccount(0, 0.2)]
    
    def newAcct(self, openingBal=0, intRate=0.02):
        self.account.append(BankAccount(openingBal, intRate))

    def makeDeposit(self, amount):
        selectedAccount = User.accountChoice(self)
        self.account[selectedAccount].deposit(amount)
        return self

    def makeWithdrawal(self, amount):
        selectedAccount = User.accountChoice(self)
        self.account[selectedAccount].withdrawal(amount)
        return self

    def userBalance(self):
        for acct in self.account:
            print(self.name + "'s current balance:", acct.displayAccountInfo())
        return self

    def transferMoney(self, user2, amount):
        self.makeWithdrawal(amount)
        user2.makeDeposit(amount)
        return self

    @staticmethod
    def accountChoice(self):
        if (len(self.account) > 1):
            userInput = input("Which account would you like to deposit into?\n", range(len(self.account)))
            return userInput
        else:
            return 0

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
        return self.balance

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


ben = User("Benjamin", "Ben@bank.com")
jack = User("Jack", "Jack@bank.com")
antony = User("Antony", "Antony@bank.com")

ben.makeDeposit(100).makeDeposit(100).makeDeposit(300).userBalance()

jack.makeDeposit(500).makeDeposit(100).makeWithdrawal(50).makeWithdrawal(20).userBalance()

antony.makeDeposit(100).makeWithdrawal(10).makeWithdrawal(50).makeWithdrawal(20).userBalance()

ben.transferMoney(antony, 1500)
ben.userBalance()
antony.userBalance()
antony.newAcct(10000,.1)
antony.userBalance()