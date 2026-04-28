import atm.account as account

def deposit_money():
    amount = int(input("Enter amount to deposit: "))

    if amount > 0:
        account.balance += amount
        account.transactions.append(f"Deposited ₹{amount}")
        print("Deposit successful")
    else:
        print("Invalid amount")