account = {}


def create_account():
    name = input("Enter account holder name: ")
    balance = float(input("Enter opening balance: "))
    account["name"] = name
    account["balance"] = balance
    print("Account created successfully.")


def deposit():
    amount = float(input("Enter deposit amount: "))
    account["balance"] += amount
    print("Amount deposited successfully.")


def withdraw():
    amount = float(input("Enter withdrawal amount: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")


def check_balance():
    print(f"Account Holder: {account.get('name', 'Not created')}")
    print(f"Balance: {account.get('balance', 0)}")


while True:
    print("\n1.Create Account 2.Deposit 3.Withdraw 4.Check Balance 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        break
    else:
        print("Invalid choice")