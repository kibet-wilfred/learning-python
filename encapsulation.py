class Bank_Account :
    balance = 0
    Acc_name = ""
    def __init__(self):
        pass

    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance


    def transfer(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount,Acc_name):
        self.balance += amount
        self .Acc_name = Acc_name
        return self.balance

    def show_balance(self):
        print("The account info are: Name-",self.Acc_name, ",Balance is",self.balance)

ac1=Bank_Account()
ac1.balance=200
ac1.Acc_name="wilfred"
ac1.show_balance()