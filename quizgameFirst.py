# The user is asked multiple questions and are given grades based on the answers they give.

print("Welcome to the quiz game. You will be asked five questions and expected to give an answer. ")

def main():

    # Defining a score variable inside the function main
    score = 0

    # Calling for function named first, error handling and grading
    while True:
        try:
            if first() == 13:
                correct()
                score += 1
            else:
                incorrect()
            break
            
        except ValueError:
            print("Please enter a valid value. ", end="\n")
    
    # Calling for second function and grading
    if second() == "central processing unit":
        correct()
        score += 1
    else:
        incorrect()
    
    # Calling for third function and grading.
    if third() == "ankara":
        correct()
        score += 1
    else:
        incorrect()
    
    # Calling for fourth function and grading.
    if fourth() == "red":
        correct()
        score += 1
    else:
        incorrect()

    # Calling for function named fifth and error handling 
    while True:
        try:
            if fifth() == 625:
                correct()
                score += 1
            else:
                incorrect()
            break
            
        except ValueError:
            print("Please enter a valid value. ", end="\n")
    
    print("Your final score is", str(score))


# Defining the first question.
def first():
    return int(input("What is the hypothenuse of a triangle whose sides are 5 and 12? ", end="\n"))

# Defining the second question.
def second():
    return input("What does CPU stand for? ")

# Defining the third question. 
def third():
    return input("What is the capital city of Turkey? ")

# Defining the fourth question.
def fourth():
    return input("Which colour has the highest wavelength? ")

# Defining the fifth question.
def fifth():
    return int(input("What is 25x25? "))

# Defining the answers
def correct():
    print("Correct!")
def incorrect():
    print("Incorrect!")

# Calling for the main function
# Providing reusability
while True:
    main()
    if input("Type exit to escape. ") == "exit":
        print("Goodbye! ")
        break





    