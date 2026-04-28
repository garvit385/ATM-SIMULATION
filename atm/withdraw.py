import atm.account as account

def withdraw_money():
    amount = int(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > account.balance:
        print("Insufficient balance")

    else:
        account.balance -= amount
        account.transactions.append(f"Withdrawn ₹{amount}")
        print("Withdrawal successful")