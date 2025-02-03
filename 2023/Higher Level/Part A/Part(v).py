# Question 16(a)
# Examination Number:


# Make the following changes to the program:

# Currently the secret number is always between 1 and 5 inclusive.

# Modify the program so that it prompts the user to enter a difficulty level – ‘E’ for easy
# and ‘H’ for hard. If the user chooses ‘H’ the secret number should be between 1 and
# 100 inclusive. A value of anything other than ‘H’ can be interpreted as easy.
# When the program is run the output may now look as follows:

from random import randint

def guess_game(max_guesses_allowed):
    # We will add the difficulty section here to ask the user if it should be easy or hard.
    # We will set a variable here to set the upper limit of the game.
    max_number = 5
    difficulty = input("Enter difficulty E(asy) or H(ard): ")

    # We want to ensure the user input regardless of case is applied. There is two ways:
    # We could use the upper() method or add both the lowercase and highercase case to the if statement.
    if (difficulty.upper() == "H"):
        max_number = 100

    secret_number = randint(1, max_number)
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
number_of_allowed_guesses = int(input("Enter the maximum number of guesses allowed: ")) 



guess_game(number_of_allowed_guesses)
