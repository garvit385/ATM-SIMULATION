from atm.deposit import deposit_money
from atm.withdraw import withdraw_money
from atm.balance import display_balance
from atm.statement import show_statement

while True:
    print("\n===== ATM MENU =====")
    print("1. Display Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Statement")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        display_balance()

    elif choice == "2":
        deposit_money()

    elif choice == "3":
        withdraw_money()

    elif choice == "4":
        show_statement()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")