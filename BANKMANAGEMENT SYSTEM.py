# BANK MANAGEMENT SYSTEM - PURE PYTHON (MENU DRIVEN)

accounts = {}

def create_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))
    accounts[acc_no] = {"name": name, "balance": balance}
    print("Account created successfully.")

def deposit_money():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter Deposit Amount: "))
    accounts[acc_no]["balance"] += amount
    print("Amount deposited successfully.")

def withdraw_money():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    amount = float(input("Enter Withdrawal Amount: "))
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount
        print("Amount withdrawn successfully.")

def check_balance():
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return
    print("Account Holder:", accounts[acc_no]["name"])
    print("Current Balance:", accounts[acc_no]["balance"])

def close_account():
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        del accounts[acc_no]
        print("Account closed successfully.")
    else:
        print("Account not found!")

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        check_balance()
    elif choice == "5":
        close_account()
    elif choice == "6":
        print("Thank you for using Bank Management System.")
        break
    else:
        print("Invalid choice! Please try again.")
