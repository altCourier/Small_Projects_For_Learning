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

    if response == "q":
        print("Goodbye!")
        break
    elif computer_response == response:
        print("It's a draw!")
    elif computer_response == "rock" and response == "paper":
        print("Human wins!")
        player += 1
    elif computer_response == "rock" and response == "scissors":
        print("Computer wins!")
        computer += 1
    elif computer_response == "paper" and response == "rock":
        print("Computer wins!")
        computer += 1
    elif computer_response == "paper" and response == "scissors":
        print("Human wins!")
        player += 1
    elif computer_response == "scissors" and response == "rock":
        print("Human wins!")
        player += 1
    elif computer_response == "scissors" and response == "paper":
        print("Computer wins!")
        computer += 1
    else:
        print("Please enter a valid option. ")