# Question 16(a)
# Examination Number:


# Make the following changes to the program:

# The program does not display a message unless the user guesses the secret number.
# Change the program so that it displays one of the following messages as a hint to the
# user:
# ‘Sorry! Your guess was too low’ or ‘Sorry! Your guess was too high’
# When the program is run the output may now look as follows:

from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0 
    user_guess = 0

    while (user_guess != secret_number):

        user_guess = int(input("Enter your guess: "))
        guess_count += 1 
        if user_guess == secret_number:
            print("Congratulations! You win!")
            print("You took", guess_count, "guesses.")
        # We will need to set up an if else statement. We will check first if the user_guess is less than the secret_number
        # We will then check if it is higher than the secret_number
        elif (user_guess < secret_number): 
            print("Sorry! Your guess was too low")
        else: # We are only using an else statement here as it is the last possible combination. We have determined it's not the correct number and it's not a lower number. An elif would also works.
            print("Sorry! Your guess was too high")
        


print("Welcome to the guessing game!")
guess_game(3)
