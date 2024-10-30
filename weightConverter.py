# Weight conversion program.

# Global variables that we need.
isRunning = True # To determine the contiunity of program.


def toLBs():
    try:
        amount = float(input("Please enter your amount of KGs."))
        if amount < 0:
            raise ValueError("The amount cannot be negative")
        else:
            print(f"{amount} Kgs is {amount*2.205:.2f}")
    except ValueError as Error:
        print(Error) 

def toKGs():
    try:
        amount = float(input("Please enter your amount of LBs."))
        if amount < 0:
            raise ValueError("The amount cannot be negative")
        else: 
            print(f"{amount} Lbs is {amount/2.205:.2f}")
    except ValueError as Error:
        print(Error)

# The main block of code.
def main():
    global isRunning
    while isRunning:
        choice = input("Please enter the amount you wish to enter.\n K for kilograms,\n L for lbs.\n X to exit the program.\n ").lower()
        if choice == "k":
            toLBs()
        elif choice == "l":
            toKGs()
        elif choice == "x":
            isRunning = False
        else:
            print("Please enter a valid response. ")

main()