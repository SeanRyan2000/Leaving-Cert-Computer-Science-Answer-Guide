# Question 16(a)
# Examination Number:


# Make the following changes to the program:

# Currently the program has no way of ending unless the user guesses the secret number.
# Change the program so that it does not allow the user more than three guesses. This is
# the value currently being passed into the function.
# Hint: You will need to change the loop so that it continues as long as the user’s guess
# is not equal to the secret number and the number of guesses is less than
# max_guesses_allowed

from random import randint

def guess_game(max_guesses_allowed):

    secret_number = randint(1, 5)
    guess_count = 0 
    user_guess = 0

# We are going to edit the loop to also inlcude max_guesses_allowed. 
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
guess_game(3)
