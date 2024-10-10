# Write a rock paper scissors game
# PC will not win in every scenario but instead will tell how many anyone won.

# Importing function from the random library
from random import choice

# Introducing to the program
print("Welcome to the rock paper scissors game! In this game you will be faced against the computer. Let's see if you win!")

player = 0
computer = 0
def evaluator():
    if computer == response:
        print(f"It's a draw with computer scoring", {computer},"and human scoring", {response},".")
    elif computer > response:
        print(f"Computer wins! With computer scoring", {computer},"and human scoring", {response},".")
    else:
        print(f"Human wins! With computer scoring", {computer},"and human scoring", {response},".")

# Defining a variable called options
options = ["rock", "paper", "scissors"]

while True:
    response = input("Please type your pick, if you wish not to continue type 'Q'! ").lower()
    computer_response = choice(options)
    
    match response:
        case "q":
            print("Goodbye!")
            break
        case response if response == computer_response:
            print("It's a draw!")
        case "paper":
            if computer_response == "rock":
                print("Human wins!")
                player += 1
            elif computer_response == "scissors":
                print("Computer wins!")
                player += 1
        case "scissors":
            if computer_response == "rock":
                print("Computer wins!")
                computer += 1
            elif computer_response == "paper":
                print("Human wins!")
                player += 1
        case "rock":
            if computer_response == "paper":
                print("Computer wins!")
                computer += 1
            elif computer_response == "scissors":
                print("Human wins!")
                player += 1
        case _:
            print("Please enter a valid option. ")
