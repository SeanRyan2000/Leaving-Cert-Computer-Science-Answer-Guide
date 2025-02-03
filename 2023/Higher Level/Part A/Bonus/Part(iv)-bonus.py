# Question 16(a)
# Examination Number:


# Make the following changes to the program:

# Currently the number of guesses that the user is allowed is hard coded to three.
# Modify the program so that the user is presented with the prompt:
# Enter the maximum number of guesses allowed.
# Store the value entered as an integer and pass this value into the function
# guess_game.

from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0 
    user_guess = 0

    while (user_guess != secret_number and guess_count < max_guesses_allowed):

        user_guess = int(input("Enter your guess: "))
        guess_count += 1 
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print("You took", guess_count, "guesses.")

        elif (user_guess < secret_number): 
            print("Sorry! Your guess was too low")
        else: 
            print("Sorry! Your guess was too high")
        
print("Welcome to the guessing game!")
# BONUS-BONUS CHALLENGE. Ensure the number is a positive int.
while True:
    try:
        number_of_allowed_guesses = int(input("Enter the maximum number of guesses allowed: "))
        break 
    except ValueError:
        print("That is not a positive int.")

guess_game(number_of_allowed_guesses)
