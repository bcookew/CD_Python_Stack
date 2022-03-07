from msilib.schema import Class


class User:
    def __init__(self,name,email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    
    def makeDeposit(self, amount):
        self.balance += amount
        return self

    def makeWithdrawal(self, amount):
        self.balance -= amount
        return self

    def userBalance(self):
        print(self.name + "'s current balance:", self.balance)
        return self

    def transferMoney(self, user2, amount):
        self.balance -= amount
        user2.balance += amount
        return self

ben = User("Benjamin", "Ben@bank.com", 1000)
jack = User("Jack", "Jack@bank.com", 500)
antony = User("Antony", "Antony@bank.com", 10000)

ben.makeDeposit(100).makeDeposit(100).makeDeposit(300).userBalance()

jack.makeDeposit(500).makeDeposit(100).makeWithdrawal(50).makeWithdrawal(20).userBalance()

antony.makeDeposit(100).makeWithdrawal(10).makeWithdrawal(50).makeWithdrawal(20).userBalance()

ben.transferMoney(antony, 1500).userBalance()
antony.userBalance()