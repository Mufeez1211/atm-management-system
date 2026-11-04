import logging
logger = logging.getLogger(__name__)
class Account:
    def __init__(self,name,pin,balance):
        self.name=name
        self.pin=pin
        self.balance=balance
        self.transactions=[]
        logger.info("Account created for customer: %s",name)
        logger.debug("Initial account balance : %.2f",balance)
    def verify_pin(self,entered_pin):
        logger.debug("Pin Verification Started")
        if entered_pin==self.pin:
            logger.info("Pin Verification successful")
            return True
        else:
            logger.warning("Incorrect Pin entered")
            return False
    def check_balance(self):
        logger.debug("Balance enquiry started")
        print(f"Available Balance : ${self.balance}")
        logger.info("Balance enquiry started")
    def withdraw(self,amount):
        logger.debug("Withdrawal requested : %.2f",amount)
        if amount<=0:
            print("Enter a valid amount")
            logger.warning("Invaild withdrawl amount: %.2f",amount)
        elif amount>self.balance:
            print("Insufficient Balance")
            logger.warning("Withdrwal declined due to insufficient balance")
        else:
            self.balance-=amount
            self.transactions.append(f"Withdrawn: ${amount}")
            print(f"{amount}withdrwan successfully!")
            print(f"Remaining Balance : {self.balance}")
            logger.info("Withdrwal successful")
            logger.debug("Remaining balance : %.2f",self.balance)
    def deposit(self,amount):
        logger.debug("Deposited requested : %.2f",amount)
        if amount<=0:
            print("Enter a Valid deposit amount")
            logger.warning("Tnvalid deposit amount : %.2f",amount)
        else:
            self.balance+=amount
            self.transactions.append(f"Deposited: ${amount}")
            print(f"${amount} deposited Successfully")
            print(f"Available Balance : ${self.balance}")
            logger.info("Deposit successful: %.2f",amount)
            logger.debug("Updated Balance: %.2f",self.balance)
    def mini_statement(self):
        logger.debug("Mini statement requested")
        print("\n=============")
        print("      MINI STATEMENT")
        print("================")
        if not self.transactions:
            print("No transactions available!")
            logger.warning("Mini statement requested with no transactions")
        else:
            for index,transaction in enumerate(self.transactions[-5:],start=1):
                print(f"{index}.{transaction}")
            logger.info("Mini statement displayed")
        print("===============")
        print(f" Available Balance : ${self.balance}")
        print("===============")
    def change_pin(self,old_pin,new_pin,confirm_pin):
        logger.debug("Pin Change Requested")
        if old_pin!=self.pin:
            print("Incorrect Old PIN!")
            logger.warning("Pin Change Failed : incorrect old PIN")
        elif len(new_pin) !=4 or not new_pin.isdigit():
            print("PIN must contain exactly 4 digits!")
            logger.warning("PIN change failed: invalid new PIN format")
        elif new_pin!=confirm_pin:
            print("New PIN and confirmation do not match!")
            logger.warning("PIN change failed : PIN confirmation mismatch")
        else:
            self.pin=new_pin
            print("PIN Changed Successfully")

