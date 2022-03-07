from msilib.schema import Class


class User:
    def __init__(self,name,email, balance=0):
        self.name = name
        self.email = email
        self.balance = balance
    
    def makeDeposit(self, amount):
        self.balance += amount

    def makeWithdrawal(self, amount):
        self.balance -= amount

    def userBalance(self):
        print(self.name + "'s current balance:", self.balance)

    def transferMoney(self, user2, amount):
        self.balance -= amount
        user2.balance += amount

ben = User("Benjamin", "Ben@bank.com")
jack = User("Jack", "Jack@bank.com")
antony = User("Antony", "Antony@bank.com")

ben.makeDeposit(100)
ben.makeDeposit(100)
ben.makeDeposit(300)
ben.userBalance()

jack.makeDeposit(500)
jack.makeDeposit(100)
jack.makeWithdrawal(50)
jack.makeWithdrawal(20)
jack.userBalance()

antony.makeDeposit(100)
antony.makeWithdrawal(10)
antony.makeWithdrawal(50)
antony.makeWithdrawal(20)
antony.userBalance()

ben.transferMoney(antony, 1500)
ben.userBalance()
antony.userBalance()