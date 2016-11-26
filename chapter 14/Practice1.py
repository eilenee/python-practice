class BankAccount:
    def __init__(self, acct_number, acct_name):
        self.acc_number = acct_number
        self.acct_name = acct_name
        self.balance = 0.0


    def displayBalance(self):
        print "The account balance is:", self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print "You deposited", amount
        print "The new balance is:", self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print "You withdrew", amount
            print "The new balance is:", self.balance
        else:
            print "You tried to withdraw", amount
            print "The account balance is:", self.balance
            print "Withdrawal denied. Not enough funds."
