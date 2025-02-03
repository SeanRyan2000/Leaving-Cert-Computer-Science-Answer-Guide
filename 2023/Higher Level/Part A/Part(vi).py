# Question 16(a)
# Examination Number:


# Make the following changes to the program:

# Currently the secret number is always between 1 and 5 inclusive.

# Modify the code so that if the user guesses a number that was already guessed the
# following message is displayed: ‘You already guessed this number.’

from random import randint

def guess_game(max_guesses_allowed):
    max_number = 5
    difficulty = input("Enter difficulty E(asy) or H(ard): ")

    if (difficulty.upper() == "H"):
        max_number = 100

    secret_number = randint(1, max_number)
    guess_count = 0 
    user_guess = 0


    # We will add a list holding the numbers already guessed:
    guessed_numbers = []

    while (user_guess != secret_number and guess_count < max_guesses_allowed):
        user_guess = int(input("Enter your guess: "))

        # Check if the number is already in the guessed_numbers
        if (user_guess in guessed_numbers):
            print("You have already guessed this number.")
        else:
            # If it is not already in the list add it to the list
            guessed_numbers.append(user_guess)

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
