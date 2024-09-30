# Write a program that generates a number and asks the user to guess it. 
# Give evaluation based on their answers
# Count how many times they tried

# Importing the random module to randomize an integer:
import random

# Introducing and taking in the numbers which the random number is going to be:
print("Welcome to the number guessing game.")

# Defining the number generator function
def numberGenerator():

    #Error handling for possible valueErrors and inputting
    #Defining a while loop for continuous input until given
    while True:
        try:
            a = int(input("Please give me the first number I can pick from. "))
            break
        except ValueError:
            print("Please enter the first integer.")
    while True:
        try:
            b = int(input("Please give me the last number I can pick from. "))
            break
        except ValueError:
            print("Please enter second integer.")
    
    #Returning a random integer given between two values
    return random.randint(a,b)

# Calling for numberGenerator function
number = numberGenerator()

# Defining a variable named score for keeping track
score = 1

# While loop for continuous guesses
while True:

    # Error handling
    while True:
        try:
            guess = int(input("Take a guess."))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Directing the user into guessing the answer and celebrating in the case of winning
    if number == guess:
        print("Good job! ")
        break
    elif number < guess:
        print("You need to go lower.")
        score += 1
    else: 
        print("You need to go higher.")
        score += 1

# Printing how many times they have guessed
print("You have tried for",str(score), "times.")
    


    