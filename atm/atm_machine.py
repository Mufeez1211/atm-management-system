
class ATMMachine:

    def __init__(self, account):
        self.account = account

    def verify_user(self):
        attempts = 3

        while attempts > 0:
            entered_pin = input("Enter your ATM PIN: ")

            if self.account.verify_pin(entered_pin):
                print("\nPIN Verified Successfully!")
                print("Welcome to ATM")
                return True

            else:
                attempts -= 1
                print("Incorrect PIN!")
                print("Attempts remaining:", attempts)

        print("ATM access blocked!")
        return False

    def show_menu(self):

        while True:
            print("\n========== ATM MENU ==========")
            print("1. Check Balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Mini Statement")
            print("5. Change PIN")
            print("6. Exit")
            print("==============================")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.account.check_balance()

            elif choice == "2":
                try:
                    amount = float(input("Enter withdrawal amount: $"))
                    self.account.withdraw(amount)
                except ValueError:
                    print("Enter numbers only!")

            elif choice == "3":
                try:
                    amount = float(input("Enter deposit amount: $"))
                    self.account.deposit(amount)
                except ValueError:
                    print("Enter numbers only!")

            elif choice == "4":
                self.account.mini_statement()

            elif choice == "5":
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                confirm_pin = input("Confirm new PIN: ")

                self.account.change_pin(
                    old_pin, new_pin, confirm_pin
                )

            elif choice == "6":
                print("Thank you for using our ATM!")
                break

            else:
                print("Invalid choice! Try again.")

    def start(self):
        if self.verify_user():
            self.show_menu()
