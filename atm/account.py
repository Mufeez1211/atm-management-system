class Account:
    def __init__(self,name,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance
        self.transactions=[]

    def verify_pin(self,entered_pin):
        if entered_pin==self.pin:
            return True
        else:
            return False
    def check_balance(self):
        print(f"Available Balance : ${self.balance}")
    def withdraw(self,amount):
        if amount<=0:
            print("Enter a valid amount")
        elif amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            self.transactions.append(f"Withdrawn: ${amount}")
            print(f"{amount}withdrwan successfully!")
            print(f"Remaining Balance : {self.balance}")
    def deposit(self,amount):
        if amount<=0:
            print("Enter a Valid deposit amount")
        else:
            self.balance+=amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited Successfully")
            print(f"Available Balance : ${self.balance}")
    def mini_statement(self):
        print("\n=============")
        print("      MINI STATEMENT")
        print("================")
        if not self.transactions:
            print("No transactions available!")
        else:
            for index,transaction in enumerate(self.transactions[-5:],start=1):
                print(f"{index}.{transaction}")
        print("===============")
        print(f" Available Balance : ${self.balance}")
        print("===============")
    def change_pin(self,old_pin,new_pin,confirm_pin):
        if old_pin!=self.pin:
            print("Incorrect Old PIN!")
        elif len(new_pin) !=4 or not new_pin.isdigit():
            print("PIN must contain exactly 4 digits!")
        else:
            self.pin=new_pin
            print("PIN Changed Successfully")

