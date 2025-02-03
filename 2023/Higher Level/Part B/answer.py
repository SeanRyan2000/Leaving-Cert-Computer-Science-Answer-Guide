# Comment
# Examination number:

from random import randint

# We are going to set user_score to 0. We are doing this outside the function
# and setting is a global variable
user_score = 0

def number_guesser():
    # Allow modification of global variable
    global user_score

    # generate random number
    secret_number = randint(1,100)

    # Allow the user input to make their guess 
    user_guess = int(input("Enter your guess: "))

    # Find the difference between the user_guess and secret_number
    # This is using the absolute value.
    # This gets the difference regardless of positive or negative value
    difference = abs(user_guess-secret_number)

    # If you do not remember the syntax you could create your own method something like:
    # 
    # if x >= y:
    #     difference = x - y
    # else:
    #     difference = y - x
    # 
    # OR
    # 
    # if difference < 0:
    #   difference = difference * -1
    #  

    print("Secret number is %d. You guessed %d. Difference is %d" %(secret_number, user_guess, difference)) 

    # Add the if statements to determine user_score.
    if (difference == 0):
        print("JACKPOT!!! You score 100 points")
        user_score += 100
    elif (difference <= 20):
        print("You score 20 points")
        user_score += 20
    else:
        print("You lose 30 points")
        user_score -= 30
    # I am printing outside the if blocks to avoid code duplication
    print("Your total score is: ", user_score)
    

number_guesser()
while True:
    play_again = input("Play again? (Y/N):")
    if (play_again.upper() == "Y"):
        number_guesser()
    else:
        break