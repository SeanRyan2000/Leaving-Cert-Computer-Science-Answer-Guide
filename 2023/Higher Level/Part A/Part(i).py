# Question 16(a)
# Examination Number:


# Make the following changes to the program:
# (i) Change the program to display an extra line of output when the user wins, showing
# the number of guesses taken.
# When the program is run the output may now look as follows: 

from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0 # We are going to use this variable. We will need to print it when the game is finished
    user_guess = 0

    while (user_guess != secret_number):

        user_guess = int(input("Enter your guess: "))
        guess_count += 1 #Increase guess_count by 1
        if user_guess == secret_number:
            print("Congratulations! You win!")
            # Print out the number of guesses taken
            print("You took", guess_count, "guesses.")

print("Welcome to the guessing game!")
guess_game(3)
