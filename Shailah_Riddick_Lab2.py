#Lab 2

#Class manages checking and saving accounts
class BankAccount:
    def __init__(self, new_name, checking_balance, savings_balance):
        self.new_name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
    def deposit_checking(self, amount):
        self.checking_balance += amount
    def deposit_savings(self, amount):
        self.savings_balance += amount
    def withdrawal_checking(self, amount):
        self.checking_balance -= amount
    def withdrawal_savings(self, amount):
        self.savings_balance -= amount
    def transfer_to_savings(self, amount):
        self.checking_balance -= amount
        self.savings_balance += amount

#Defining the variables
new_name = input("Enter your name: ")
account = BankAccount('Mickey', 500, 1000)

#Defines the methods
account.checking_balance =500
account.savings_balance =500
account.withdrawal_checking(100)
account.withdrawal_savings(100)
account.transfer_to_savings(300)

#Prints the bank account info
print(account.new_name)
print(f'${account.checking_balance:.2f}')
print(f'${account.savings_balance:.2f}')

