# Python banking program: 

# These are the status variables we have:
balance = 0
isRunning = True
transictions = []

# This function will showcase the balance the user has.
def showBalance():
    print(f"Your balance is {balance:.2f} TL. ")

# This function will enter an amount of money the user wishes to enter.
def deposit():
    global balance
    global transictions
    
    # Error handling and taking in inputs.
    try: 
        amount = float(input("Please enter the amount you wish to deposit. "))
        if amount < 0:
            raise ValueError("Amount must be positive.")
        balance += amount
        transictions.append(f"Deposited {amount:.2f}")
        print(f"Successfully deposited {amount} TL")

    except ValueError as e:
        print(e)


# This function will take some amount of money the user has.
def withdraw():
    global balance
    global transictions

    # Error handling.
    try:
        amount = float(input("Please enter the amount you wish to withdraw. "))
        if amount < 0:
            raise ValueError("Amount must be positive. ")
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount

        transictions.append(f"Withdrew {amount:.2f}")
        print(f"Successfully withdrew {amount} TL")

    except ValueError as Error:
        print(Error)

# Where the main code block is. 
def showTransictions():
    global transictions
    global balance
    if transictions:
        for transaction in transictions:
            print(transaction)
            print(f"Last balance is: {balance}")
    else:
        print("No history to display. ")

def main():
    global isRunning
    while isRunning:

        print(" Python Banking Program\n")
        print("1. Show Balance")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Show Transictions ")
        print("5. Exit ")

        choice = input("Please enter your choice (1-5)\n")

        if choice == "1":
            showBalance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            showTransictions()
        elif choice == '5':
            print("Goodbye! ")
            isRunning = False
        else:
            print("\nPlease enter a valid response. \n")

main()