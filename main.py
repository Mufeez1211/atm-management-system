from atm.account import Account
from atm.atm_machine import ATMMachine
from atm.log_config import setup_logging
setup_logging()
my_account=Account("Syed","2565",25000)
my_atm=ATMMachine(my_account)
my_atm.start()
