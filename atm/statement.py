import atm.account as account

def show_statement():
    print("\nTransaction History:")

    if not account.transactions:
        print("No transactions yet")
    else:
        for t in account.transactions:
            print(t)