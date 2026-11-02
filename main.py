from atm.account import Account
from atm.atm_machine import ATMMachine
my_account=Account("Syed","2565",25000)
my_atm=ATMMachine(my_account)
my_atm.start()
