class BankAccount(object):
    def __init__(self, name):
        if not name:
            raise ValueError("Account holder name cannot be empty.")
        self.name = name
        self.balance = 0

    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)

    def show_balance(self):
        print("Balance: $%.2f" % self.balance)

    def update_name(self, new_name):
        self.name = new_name
        print("Account holder name updated to %s" % self.name)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than $0")
            return
        else:
            print("You have deposited $%.2f" % amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("You cannot withdraw $%.2f as there is only $%.2f in your account" % (amount, self.balance))
            return
        else:
            print("You have withdrawn $%.2f" % amount)
            self.balance -= amount
            self.show_balance()

