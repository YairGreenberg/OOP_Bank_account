

class BankAccount:
    def __init__(self,account_holder:str,initial_balance:float):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def transfer_funds(self,other_account,amount):
        if other_account.initial_balance - amount > 0:
            other_account.initial_balance -= amount
            print("The transfer was successful!")
        else:
            print("I'm making a payment but there's not enough money in my account.")

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: {self.initial_balance}"




if __name__=="__main__":
    ba1 = BankAccount("yair greenberg",1000)
    print(f"This is the initial state:\n {ba1}")
    ba2 = BankAccount("efrat greenberg ", 25000)
    print(f"This is the initial state:\n {ba2}")
    ba1.transfer_funds(ba1,600)
    print(f"Account status after transferring the money!\n {ba1} ")
    ba2.transfer_funds(ba2,1400)
    print(f"Account status after transferring the money!\n {ba2} ")
